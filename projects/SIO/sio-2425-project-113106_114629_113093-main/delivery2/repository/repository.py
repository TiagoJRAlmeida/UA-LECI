from flask import Flask, request
import os
import json
import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
import signal
from repository_auxiliary_functions import *
from datetime import datetime, timedelta

app = Flask(__name__)

organizations = {}
documents = {}
sessions = {}
password = "pass1234"

# Adicionar as chaves publica e privada do Repositório em ficheiros separados dentro 
# da pasta do Repositório (para segurança)
current_dir = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(f"{current_dir}/rep_pub_key.pem") or not os.path.exists(f"{current_dir}/rep_priv_key.pem"):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    ENCRYPTED_REP_PRIV_KEY = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

    REP_PUB_KEY = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    with open(f"{current_dir}/rep_pub_key.pem", "wb") as pubk_file:
        pubk_file.write(REP_PUB_KEY)

    with open(f"{current_dir}/rep_priv_key.pem", "wb") as privk_file:
        privk_file.write(ENCRYPTED_REP_PRIV_KEY)

    with open(f"{current_dir}/../rep_pub_key.pem", "wb") as pubk_file:
        pubk_file.write(REP_PUB_KEY)

# Ficheiros para salvar os dicionários
org_file_path = f"{current_dir}/organizations.json"
documents_file_path = f"{current_dir}/documents.json"
sessions_file_path = f"{current_dir}/sessions.json"

# Carregar os ficheiros nos dicionários
def load_state():
    global organizations, documents, sessions
    if os.path.exists(org_file_path):
        with open(org_file_path, "r") as org_file:
            organizations = json.load(org_file)
    
    if os.path.exists(documents_file_path):
        with open(documents_file_path, "r") as documents_file:
            documents = json.load(documents_file)

    if os.path.exists(sessions_file_path):
        with open(sessions_file_path, "r") as sessions_file:
            sessions = json.load(sessions_file)


# Salvar os dicionários em ficheiros
def save_state():
    # Save organizations
    with open(org_file_path, "w") as org_file:
        json.dump(organizations, org_file)
    
    # Save documents
    with open(documents_file_path, "w") as documents_file:
        json.dump(documents, documents_file)

    # Save sessions
    with open(sessions_file_path, "w") as sessions_file:
        json.dump(sessions, sessions_file)


# Graceful shutdown handler
def shutdown_handler(signum, frame):
    print("Shutting down... Saving state.")
    save_state()
    os._exit(0)


# Register signal handlers
signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

load_state()

# <--- Anonymous API Routes --->
@app.route("/organization/create", methods=["POST"])
def org_create():
    data = request.get_json()
    org_name = data["organization_name"]
    manager_subject = data["manager_subject"]
    username = manager_subject[0]
    name = manager_subject[1]
    email = manager_subject[2]
    public_key = manager_subject[3]

    # Verificar se a nova organização já existe
    if org_name in organizations:
        return json.dumps({"Error": "Organization name already exists"}), 400

    # Adicionar a nova organização
    organizations[org_name] = {
        "SUBJECTS": {
            username: {
                "FULL_NAME": name,
                "EMAIL": email,
                "PUBLIC_KEY": public_key,
                "STATUS": "ACTIVE",
                "ROLES": ["MANAGER"]
            }
        },
        "ACL": {
            "MANAGER": {
                "PERMISSIONS": [
                    "ROLE_ACL",
                    "SUBJECT_NEW",
                    "SUBJECT_DOWN",
                    "SUBJECT_UP",
                    "DOC_NEW",
                    "ROLE_NEW",
                    "ROLE_DOWN",
                    "ROLE_UP",
                    "ROLE_MOD"
                ],
                "STATUS": "ACTIVE"
            }
        },
        "SESSION_IDS": [],
        "DOCUMENT_HANDLES": []
    }
    
    return json.dumps({"Success": "Organization created"}), 200


@app.route("/organization/list")
def org_list():
    all_orgs = [org for org in organizations]
    return json.dumps(all_orgs)


@app.route("/session/create", methods=["POST"])
def org_new_session():
    data = request.get_json()
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_encrypted_key = base64.b64decode(data["encrypted_key"])
    received_hmac = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])
    received_signature = base64.b64decode(data["signature"])

    # Ler a chave do repositório
    with open(f"{current_dir}/rep_priv_key.pem", "rb") as pkey_file:
        rep_priv_key = load_pem_private_key(
            pkey_file.read(),
            password=password.encode()
        )

    # Descifrar a encrypted_key com a chave privada do servidor
    decrypted_key = rep_priv_key.decrypt(
        received_encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Dividir a chave em duas novamente
    new_encryption_key = decrypted_key[0:16]
    new_integrity_key = decrypted_key[16:]

    # Descifrar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, new_encryption_key, received_iv))

    # verificar se a organização existe e se o username e public key 
    # existem dentro da organização.
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    public_key = decrypted_payload["public_key"]

    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    elif username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    elif public_key != organizations[organization_name]["SUBJECTS"][username]["PUBLIC_KEY"]:
        return json.dumps({"Error": "Public key not compatible"}), 400

    # Descifrar a assinatura com a publica do cliente para ver se está correto (para verificar se foi enviado pela pessoa certa)
    rsa_public_key = load_pem_public_key(base64.b64decode(public_key)) 
    try:
        rsa_public_key.verify(
            received_signature,
            received_encrypted_key,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except Exception as e:
        return json.dumps({"Error": f"Signature verification failed: {str(e)}"}), 400

    # Calcular o hmac
    calculated_hmac_signature = calculate_hmac(received_encrypted_key, new_integrity_key)
    
    # Verificar se o HMAC está correto
    if calculated_hmac_signature != received_hmac:
        return json.dumps({"Error": "HMAC not the same."}), 400

    # Criar um session_id os dados da sessão
    session_id = str(os.urandom(16))
    while session_id in sessions:
        session_id = str(os.urandom(16))

    # Definir o tempo em que a sessão expira
    current_time = datetime.now()
    expiry_time = current_time + timedelta(hours=1)
    expiry_time = expiry_time.strftime("%d-%m-%Y %H:%M:%S")

    # Guardar os dados da sessão
    sessions[session_id] = {
        "SUBJECT": username,
        "ORG_NAME": organization_name,
        "ROLES": [],
        "KEYS": {
            "ENCRYPTION_KEY": base64.b64encode(new_encryption_key).decode(),  
            "INTEGRITY_KEY": base64.b64encode(new_integrity_key).decode(), 
            "NONCE": base64.b64encode(received_nonce).decode()
        },
        "EXPIRY_TIME": expiry_time
    }

    organizations[organization_name]["SESSION_IDS"].append(session_id)

    # Avisar o cliente de sucesso e enviar o session_id e o expiry_time
    return json.dumps({"session_id": session_id, "expiry_time": expiry_time}), 200


@app.route("/doc/get/file_by_handle", methods=["POST"])
def get_doc_content_by_handle():
    data = request.get_json()
    file_handle = data["file_handle"]

    # Procurar o ficheiro pedido
    file_path = f"{current_dir}/docs/{file_handle}"
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return json.dumps({"encrypted_file_content": base64.b64encode(f.read()).decode()}), 200
            
    return json.dumps({"Error": "File handle doesn't exist"}), 400
# <-------------------------------->


# <--- Authenticated API Routes --->
# rep_assume_role
@app.route("/role/assume", methods=["POST"])
def role_assume():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    role_to_assume = decrypted_payload["role"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o role existe dentro da organização
    if role_to_assume not in organizations[organization_name]["ACL"]:
        return json.dumps({"Error": "Role doesn't exist"}), 400

    # Verificar se o subject tem permissão para assumir a role
    if role_to_assume not in organizations[organization_name]["SUBJECTS"][username]["ROLES"]:
        return json.dumps({"Error": "Cannot assume role because subject doesn't have the right to this role"}), 400
    
    # Adicionar essa role ao subject nessa session, caso ele não o tenha ainda
    if role_to_assume not in sessions[received_session_id]["ROLES"]: 
        sessions[received_session_id]["ROLES"].append(role_to_assume)
        return json.dumps({"status": "success", "message": "Role assumed"}), 200
    
    return json.dumps({"Error": "Already have that role."}), 400


# rep_drop_role
@app.route("/role/drop", methods=["POST"])
def role_drop():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    role_to_drop = decrypted_payload["role"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    if role_to_drop not in organizations[organization_name]["ACL"]:
        return json.dumps({"Error": "Role doesn't exist"}), 400
    
    # Pegar as roles atuais do subject na sua sessão
    subject_roles = [roles for roles in sessions[received_session_id]["ROLES"]]

    # Verificar se o subject tem essa role
    if role_to_drop not in subject_roles:
        return json.dumps({"Error": "Cannot drop role because subject doesn't have this role"}), 400
    
    # Remover a role do subject nessa session
    sessions[received_session_id]["ROLES"].remove(role_to_drop)

    return json.dumps({"status": "success", "message": "Role dropped"}), 200


# rep_list_roles e rep_list_subject_roles
@app.route("/role/list", methods=["POST"])
def role_list():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    filter_username = decrypted_payload["filter_username"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    roles_and_status = {}
    # Se não houver username de filtro, devolver todos os roles da session e o seu status na organização
    if not filter_username:
        for role in sessions[received_session_id]["ROLES"]:
            roles_and_status[role] = organizations[organization_name]["ACL"][role]["STATUS"]
        return json.dumps(roles_and_status), 200
    # Se houver username de filtro
    else:
        # Verificar se o username de filtro existe
        if filter_username in organizations[organization_name]["SUBJECTS"]:
            # Procurar as roles do filter_username
            for role in organizations[organization_name]["SUBJECTS"][filter_username]["ROLES"]:
                roles_and_status[role] = organizations[organization_name]["ACL"][role]["STATUS"]
            return json.dumps(roles_and_status), 200

        return json.dumps({"Error": "Username doesn't exist"}), 400
    

# rep_list_subjects
@app.route("/subject/list", methods=["POST"])
def org_list_subjects():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    filter_username = decrypted_payload["filter_username"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Se o username usado para filter não existir na organização, returnar erro
    elif filter_username and filter_username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username used for filter doesn't exist"}), 400
    
    # Filtrar os users, se necessário, e devolver ao cliente a lista
    if filter_username and filter_username in organizations[organization_name]["SUBJECTS"]:
        subject_status = organizations[organization_name]["SUBJECTS"][filter_username]["STATUS"]
        return json.dumps({filter_username: subject_status}), 200

    # Se não for dado um username como filtro, devolver todos os usernames e status de todos os
    # subjects da organização
    elif not filter_username:
        usernames_and_status = {}
        for subject_username in organizations[organization_name]["SUBJECTS"]:
            usernames_and_status[subject_username] = organizations[organization_name]["SUBJECTS"][subject_username]["STATUS"]
        return json.dumps(usernames_and_status), 200


# rep_list_role_subjects
@app.route("/role/list/subjects", methods=["POST"])
def role_list_subject():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    filter_role = decrypted_payload["filter_role"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o role a filtrar os subjects existe
    if filter_role not in organizations[organization_name]["ACL"]:
        return json.dumps({"Error": "Role doesn't exist"}), 400
    
    subjects_list = [subject for subject in organizations[organization_name]["SUBJECTS"] if filter_role in organizations[organization_name]["SUBJECTS"][subject]["ROLES"]]
    
    return json.dumps(subjects_list), 200


# rep_list_role_permissions
@app.route("/role/list/permissions", methods=["POST"])
def role_list_permissions():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    filter_role = decrypted_payload["filter_role"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o role a filtrar os subjects existe
    if filter_role not in organizations[organization_name]["ACL"]:
        return json.dumps({"Error": "Role doesn't exist"}), 400
    
    role_permissions = organizations[organization_name]["ACL"][filter_role]["PERMISSIONS"]
    
    return json.dumps(role_permissions), 200


# rep_list_permission_roles
@app.route("/permission/list/role", methods=["POST"])
def permission_list_roles():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    filter_permission = decrypted_payload["filter_permission"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se a permissão a filtrar é uma permissão da organização ou dos documentos
    if filter_permission in organizations[organization_name]["ACL"]["MANAGER"]["PERMISSIONS"]:
        roles = [role for role in organizations[organization_name]["ACL"] if filter_permission in organizations[organization_name]["ACL"][role]["PERMISSIONS"]]
        return json.dumps({"type": "Organization roles", "roles": roles}), 200
    
    elif filter_permission in ["DOC_ACL", "DOC_READ", "DOC_DELETE"]:
        docs_and_roles = {}
        for document_handle in organizations[organization_name]["DOCUMENT_HANDLES"]:
            for role in documents[document_handle]["ACL"]:
                if filter_permission in documents[document_handle]["ACL"][role]:
                    if documents[document_handle]["NAME"] not in docs_and_roles:
                        docs_and_roles[documents[document_handle]["NAME"]] = [role]
                    else:
                        docs_and_roles[documents[document_handle]["NAME"]].append(role)

        return json.dumps({"type": "Documents roles", "roles": docs_and_roles}), 200
    
    else:
        return json.dumps({"Error": "Permission doesn't exist"}), 400
    

# rep_list_docs
@app.route("/doc/list", methods=["POST"])
def org_list_docs():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    filter_username = decrypted_payload["filter_username"]
    filter_date_relation = decrypted_payload["filter_date_relation"]
    filter_date = decrypted_payload["filter_date"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Se não houver filtro de username ou data, enviar todos os docs
    if not any([filter_username, filter_date_relation, filter_date]):
        document_handles = organizations[organization_name]["DOCUMENT_HANDLES"]
        documents_list = [
            (documents[document_handle]["NAME"], 
            documents[document_handle]["CREATOR"], 
            documents[document_handle]["CREATION_DATE"])
            for document_handle in document_handles
        ]
        return json.dumps({"documents": documents_list}), 200

    # Se houver username mas não data 
    elif filter_username and not all([filter_date_relation, filter_date]):
        document_handles = organizations[organization_name]["DOCUMENT_HANDLES"]
        documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if documents[document_handle]["CREATOR"] == filter_username
                ]
        return json.dumps({"documents": documents_list}), 200
    
    # Se houver data mas não username
    elif not filter_username and all([filter_date_relation, filter_date]):
        document_handles = organizations[organization_name]["DOCUMENT_HANDLES"]
        if filter_date_relation == "nt":
            documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if documents[document_handle]["CREATION_DATE"] > filter_date
                ]
            return json.dumps({"documents": documents_list}), 200

        elif filter_date_relation == "ot":  
            documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if documents[document_handle]["CREATION_DATE"] < filter_date
                ]
            return json.dumps({"documents": documents_list}), 200

        elif filter_date_relation == "et":
            documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if documents[document_handle]["CREATION_DATE"] == filter_date
                ]
            return json.dumps({"documents": documents_list}), 200

        else:
            return json.dumps({"Error": "Date relation filter not valid. Must be: [nt/ot/et]"}), 400
        
    # Se for dado todos os argumentos
    else:
        document_handles = organizations[organization_name]["DOCUMENT_HANDLES"]
        if filter_date_relation == "nt":
            documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if (documents[document_handle]["CREATOR"] == filter_username
                        and documents[document_handle]["CREATION_DATE"] > filter_date)
                ]
            return json.dumps({"documents": documents_list}), 200

        elif filter_date_relation == "ot":  
            documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if (documents[document_handle]["CREATOR"] == filter_username
                        and documents[document_handle]["CREATION_DATE"] < filter_date)
                ]
            return json.dumps({"documents": documents_list}), 200

        elif filter_date_relation == "et":
            documents_list = [
                    (documents[document_handle]["NAME"], 
                    documents[document_handle]["CREATOR"], 
                    documents[document_handle]["CREATION_DATE"])
                    for document_handle in document_handles
                    if (documents[document_handle]["CREATOR"] == filter_username
                        and documents[document_handle]["CREATION_DATE"] == filter_date)
                ]
            return json.dumps({"documents": documents_list}), 200

        else:
            return json.dumps({"Error": "Date relation filter not valid. Must be: [nt/ot/et]"}), 400
# <-------------------------------->


# <--- Authorized API Routes --->
@app.route("/subject/create", methods=["POST"])
def org_new_subject():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    new_subject = decrypted_payload["new_subject"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o username não existe já
    if new_subject[0] in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username already exist"}), 400
        
    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
    
    # Verificar se essa role tem a permissão
    for role in active_subject_roles:
        if "SUBJECT_NEW" in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:

            # Adicionar o novo subject
            organizations[organization_name]["SUBJECTS"][new_subject[0]] = {
                "FULL_NAME": new_subject[1],
                "EMAIL": new_subject[2],
                "PUBLIC_KEY": new_subject[3],
                "STATUS": "ACTIVE",
                "ROLES": []
            }

            return json.dumps({"Success": "Subject added"}), 200
    
    return json.dumps({"Error": "You don't have the necessary permission"}), 400


@app.route("/subjects/suspend", methods=["POST"])
def org_suspend_subject():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    subject_to_suspend = decrypted_payload["subject_to_suspend"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o subject a mudar o status existe
    if subject_to_suspend not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Subject to change doesn't exist"}), 400
    
    # Se o subject a ser suspenso for o unico com a role manager, este não pode ser suspenso
    if "MANAGER" in organizations[organization_name]["SUBJECTS"][subject_to_suspend]["ROLES"]:
        manager_subjects = [subject for subject in organizations[organization_name]["SUBJECTS"] if "MANAGER" in organizations[organization_name]["SUBJECTS"][subject]["ROLES"] and subject != subject_to_suspend]
        if not manager_subjects:
            return json.dumps({"Error": "Not possible to suspend subject. There must always be a manager in a organization."}), 400

    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
    
    # Verificar se essa role tem a permissão
    for role in active_subject_roles:
        if "SUBJECT_DOWN" in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:
            
            organizations[organization_name]["SUBJECTS"][subject_to_suspend]["STATUS"] = "SUSPENDED"

            return json.dumps({"Success": "Subject status changed to suspended"}), 200
    
    return json.dumps({"Error": "You don't have the necessary permission"}), 400


@app.route("/subjects/activate", methods=["POST"])
def org_activate_subject():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    subject_to_activate = decrypted_payload["subject_to_activate"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o subject a mudar o status existe
    if subject_to_activate not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Subject to change doesn't exist"}), 400
    
    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
    
    # Verificar se essa role tem a permissão
    for role in active_subject_roles:
        if "SUBJECT_UP" in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:
            
            organizations[organization_name]["SUBJECTS"][subject_to_activate]["STATUS"] = "ACTIVE"

            return json.dumps({"Success": "Subject status changed to active"}), 200

    return json.dumps({"Error": "You don't have the necessary permission"}), 400


@app.route("/role/add", methods=["POST"])
def role_add():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    new_role = decrypted_payload["role"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400

    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
    
    # Verificar se essa role tem a permissão
    for role in active_subject_roles:
        if "ROLE_NEW" in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:
            
            # Verificar se a role que está a ser adicionada já existe
            if new_role in organizations[organization_name]["ACL"]:
                return json.dumps({"Error": "Role already exists."}), 400
            
            organizations[organization_name]["ACL"][new_role] = {
                "PERMISSIONS": [], 
                "STATUS": "ACTIVE"
            }

            return json.dumps({"status": "success", "message": "Role created"}), 200

    return json.dumps({"Error": "Subject missing permissions to add role"}), 400


@app.route("/role/change/status", methods=["POST"])
def role_change_status():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    role = decrypted_payload["role"]
    operation = decrypted_payload["operation"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    if operation == "suspend":
        subject_active_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
        for subject_role in subject_active_roles:
            if "ROLE_DOWN" in organizations[organization_name]["ACL"][subject_role]["PERMISSIONS"]:
                organizations[organization_name]["ACL"][role]["STATUS"] = "SUSPENDED"
                return json.dumps({"status": "success", "message": "Role suspended"}), 200
        return json.dumps({"Error": "Missing ROLE_DOWN permission"}), 400
    
    elif operation == "reactivate":
        subject_active_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
        for subject_role in subject_active_roles:
            if "ROLE_UP" in organizations[organization_name]["ACL"][subject_role]["PERMISSIONS"]:
                organizations[organization_name]["ACL"][role]["STATUS"] = "ACTIVE"
                return json.dumps({"status": "success", "message": "Role reactivated"}), 200
        return json.dumps({"Error": "Missing ROLE_UP permission"}), 400

    else:
        return json.dumps({"Error": "Operation invalid"}), 400
    

@app.route("/role/add/permission", methods=["POST"])
def role_add_permission():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    role = decrypted_payload["role"]
    username_or_permission = decrypted_payload["username_or_permission"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o subject tem a permissão necessária
    active_subject_roles = [subject_role for subject_role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][subject_role]["STATUS"] == "ACTIVE"]
    for subject_role in active_subject_roles:
        if "ROLE_MOD" in organizations[organization_name]["ACL"][subject_role]["PERMISSIONS"]:

            # Verificar se o argumento recebido é um username ou uma permissão
            if username_or_permission in organizations[organization_name]["ACL"]["MANAGER"]["PERMISSIONS"]:
                # Significa que é uma permissão
                new_permission = username_or_permission
                
                # Verificar se a role não tem a permissão já
                if new_permission in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:
                    return json.dumps({"Error": "Role already has permission"}), 400
                
                # Adicionar permissão
                organizations[organization_name]["ACL"][role]["PERMISSIONS"].append(new_permission)
                return json.dumps({"status": "success", "message": "Permission added to role"}), 200
            
            elif username_or_permission in organizations[organization_name]["SUBJECTS"]:
                # Significa que é um username
                username = username_or_permission

                # Verificar se o username não tem já a role
                if role in organizations[organization_name]["SUBJECTS"][username]["ROLES"]:
                    return json.dumps({"Error": f"Subject already has the role"}), 400
                
                # Adicionar role ao subject
                organizations[organization_name]["SUBJECTS"][username]["ROLES"].append(role)
                return json.dumps({"status": "success", "message": "Role added to subject"}), 200

            else:
                return json.dumps({"Error": "Last argument must be either a valid username or permission"}), 400
            
    return json.dumps({"Error": "You must have the right permissions"}), 400


@app.route("/role/remove/permission", methods=["POST"])
def role_remove_permission():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    role = decrypted_payload["role"]
    username_or_permission = decrypted_payload["username_or_permission"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Verificar se o subject tem a permissão necessária
    active_subject_roles = [subject_role for subject_role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][subject_role]["STATUS"] == "ACTIVE"]
    for subject_role in active_subject_roles:
        if "ROLE_MOD" in organizations[organization_name]["ACL"][subject_role]["PERMISSIONS"]:
    
            # Verificar se o argumento recebido é um username ou uma permissão
            if username_or_permission in organizations[organization_name]["ACL"]["MANAGER"]["PERMISSIONS"]:
                # Significa que é uma permissão
                new_permission = username_or_permission
                
                # Verificar se a role tem a permissão
                if new_permission not in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:
                    return json.dumps({"Error": "Role doesn't have that permission"}), 400
                
                # Remover permissão
                organizations[organization_name]["ACL"][role]["PERMISSIONS"].remove(new_permission)
                return json.dumps({"status": "success", "message": "Permission removed from role"}), 200
            
            elif username_or_permission in organizations[organization_name]["SUBJECTS"]:
                # Significa que é um username
                username = username_or_permission

                # Verificar se o username tem a role
                if role not in organizations[organization_name]["SUBJECTS"][username]["ROLES"]:
                    return json.dumps({"Error": "Subject doesn't have the role"}), 400
                
                # Retirar role do subject
                organizations[organization_name]["SUBJECTS"][username]["ROLES"].remove(role)
                return json.dumps({"status": "success", "message": "Role removed from subject"}), 200

            else:
                return json.dumps({"Error": "Last argument must be either a valid username or permission"}), 400
            
    return json.dumps({"Error": "You must have the right permissions"}), 400


@app.route("/doc/create", methods=["POST"])
def doc_new():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_encrypted_document_content = base64.b64decode(data["encrypted_document_content"])
    received_payload_iv = base64.b64decode(data["payload_iv"])
    received_nonce = base64.b64decode(data["nonce"])
    received_hmac_signature = base64.b64decode(data["hmac"])

    
    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_payload_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + received_encrypted_document_content + payload_bytes + received_payload_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    secret_key = base64.b64decode(decrypted_payload["secret_key"])
    document_iv = base64.b64decode(decrypted_payload["document_iv"])
    document_name = decrypted_payload["document_name"]
    file_handle = decrypted_payload["file_handle"]
    algorithm = decrypted_payload["algorithm"]
    
    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]
    
    # Verificar se essa role tem a permissão
    for role in active_subject_roles:
        if "DOC_NEW" in organizations[organization_name]["ACL"][role]["PERMISSIONS"]:

            # Ler a chave do repositório
            with open(f"{current_dir}/rep_pub_key.pem", "rb") as pkey_file:
                rep_pub_key = load_pem_public_key(pkey_file.read())

            # Encriptar a chave secreta com a pública do server
            encrypted_key = rep_pub_key.encrypt(
                secret_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )    

            # Encriptar a informação do algoritmo com a pública do server
            encrypted_alg = rep_pub_key.encrypt(
                algorithm.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )   

            # Criar o document_handle: hash do nome do documento + nome da organização
            digest = hashes.Hash(hashes.SHA256())
            message = document_name.encode() + organization_name.encode()
            digest.update(message)
            document_handle = digest.finalize()

            # Verificar se o document_handle é válido (ou seja, se o document_name já existe na organization)
            if base64.b64encode(document_handle).decode() in documents:
                return json.dumps({"Error": "Document name already exists in the organization"}), 400
            
            # Adicionar o diretório /docs caso não exista
            docs_dir_path = f"{current_dir}/docs"
            if not os.path.exists(docs_dir_path):
                os.mkdir(docs_dir_path)

            file_handle = file_handle.replace("/", "_")
            file_path = f"{docs_dir_path}/{file_handle}"

            with open(file_path, "wb") as f:
                f.write(received_encrypted_document_content)
            
            # Definir o tempo de criação do documento 
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            documents[base64.b64encode(document_handle).decode()] = {
                "NAME": document_name,
                "CREATION_DATE": current_time,
                "CREATOR": username,
                "ORG_NAME": organization_name,
                "FILE_HANDLE": file_handle,
                "ACL": {
                    "MANAGER": ["DOC_ACL", "DOC_READ", "DOC_DELETE"]
                },
                "DELETER": None,
                "ALG": base64.b64encode(encrypted_alg).decode(),
                "KEY": base64.b64encode(encrypted_key).decode(),
                "IV": base64.b64encode(document_iv).decode()
            }

            organizations[organization_name]["DOCUMENT_HANDLES"].append(base64.b64encode(document_handle).decode())

            return json.dumps({"status": "success", "message": "Document added"}), 200
        
    return json.dumps({"Error": "Missing permissions to add document"}), 400
    

@app.route("/doc/get/metadata", methods=["POST"])
def doc_get_doc_metadata():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_payload_iv = base64.b64decode(data["payload_iv"])
    received_nonce = base64.b64decode(data["nonce"])
    received_hmac_signature = base64.b64decode(data["hmac"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_payload_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_payload_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    document_name = decrypted_payload["document_name"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400

    # Criar o document_handle: hash do nome do documento + nome da organização
    digest = hashes.Hash(hashes.SHA256())
    message = document_name.encode() + organization_name.encode()
    digest.update(message)
    document_handle = base64.b64encode(digest.finalize()).decode()

    # Verificar se o document_handle é válido
    if document_handle not in documents:
        return json.dumps({"Error": "Document doesn't exist"}), 400
    
    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]

    # Verificar se tem a permissão necessária
    for role in active_subject_roles:
        if role in documents[document_handle]["ACL"] and "DOC_READ" in documents[document_handle]["ACL"][role]:

            # Ler a chave do repositório
            with open(f"{current_dir}/rep_priv_key.pem", "rb") as pkey_file:
                rep_priv_key = load_pem_private_key(
                    pkey_file.read(),
                    password=password.encode()
                )

            # Descifrar o "ALG"
            decrypted_alg = rep_priv_key.decrypt(
                base64.b64decode(documents[document_handle]["ALG"]),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Descifrar a "KEY"
            decrypted_key = rep_priv_key.decrypt(
                base64.b64decode(documents[document_handle]["KEY"]),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Preparar o payload com os metadados do documento
            payload = {
                "document_name": documents[document_handle]["NAME"],
                "creation_date": documents[document_handle]["CREATION_DATE"],
                "creator": documents[document_handle]["CREATOR"],
                "organization_name": documents[document_handle]["ORG_NAME"],
                "file_handle": documents[document_handle]["FILE_HANDLE"],
                "acl": documents[document_handle]["ACL"],
                "deleter": documents[document_handle]["DELETER"],
                "algorithm": base64.b64encode(decrypted_alg).decode(),
                "key": base64.b64encode(decrypted_key).decode(),
                "iv": documents[document_handle]["IV"]
            }

            # Encriptar o payload com os metadados com a chave de sessão
            payload_bytes = json.dumps(payload).encode()
            encrypted_payload, payload_iv = encrypt_data_AES_CBC(payload_bytes, encryption_key)

            # Gerar um NONCE
            nonce = os.urandom(16)
            while base64.b64encode(nonce).decode() in sessions[received_session_id]["KEYS"]["NONCE"]:
                nonce = os.urandom(16)

            # Gerar o hmac
            message = payload_bytes + payload_iv + nonce
            hmac_signature = calculate_hmac(message, integrity_key)

            # Possivelmente adicionar uma assinatura digital para segurança extra

            # Preparar o payload final e enviar
            final_payload = {
                "encrypted_payload": base64.b64encode(encrypted_payload).decode(),
                "payload_iv": base64.b64encode(payload_iv).decode(),
                "nonce": base64.b64encode(nonce).decode(),
                "hmac": base64.b64encode(hmac_signature).decode()
            }

            return json.dumps(final_payload), 200
    
    return json.dumps({"Error": "Missing permissions to read document metadata"}), 400


@app.route("/doc/clear/file-handle", methods=["POST"])
def doc_clear_file_handle():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    document_name = decrypted_payload["document_name"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Criar o document_handle: hash do nome do documento + nome da organização
    digest = hashes.Hash(hashes.SHA256())
    message = document_name.encode() + organization_name.encode()
    digest.update(message)
    document_handle = base64.b64encode(digest.finalize()).decode()

    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]

    # Verificar se tem a permissão necessária
    for role in active_subject_roles:
        if role in documents[document_handle]["ACL"] and "DOC_DELETE" in documents[document_handle]["ACL"][role]:

            # Verificar se o document_handle é válido (ou seja, se o document_name existe na organization)
            if document_handle not in documents:
                return json.dumps({"Error": "Document name doesn't exists in the organization"}), 400
            
            # Limpar o file_handle
            documents[document_handle]["FILE_HANDLE"] = None

            return json.dumps({"status": "success", "message": "Document deleted"}), 200

    return json.dumps({"Error": "Missing permissions to delete file handle"}), 400


@app.route("/doc/change/acl", methods=["POST"])
def doc_change_acl():
    data = request.get_json()
    received_session_id = data["session_id"]
    received_encrypted_payload = base64.b64decode(data["encrypted_payload"])
    received_hmac_signature = base64.b64decode(data["hmac"])
    received_nonce = base64.b64decode(data["nonce"])
    received_iv = base64.b64decode(data["iv"])

    # Verificar se o session ID é valido
    if received_session_id not in sessions:
        return json.dumps({"Error": "Session ID not valid"}), 400
    
    # Verificar se a sessão está dentro do tempo válido
    current_time = datetime.now()
    expiry_time = datetime.strptime(sessions[received_session_id]["EXPIRY_TIME"], "%d-%m-%Y %H:%M:%S")
    if current_time > expiry_time:
        sessions.pop(received_session_id)
        return json.dumps({"Error": "Session expiry time reached. Create a new session."}), 400

    # Verificar se o nonce é válido
    correct_nonce = calculate_next_nonce(base64.b64decode(sessions[received_session_id]["KEYS"]["NONCE"]))
    if received_nonce != correct_nonce:
        return json.dumps({"Error": "Nonce not valid"}), 400
    sessions[received_session_id]["KEYS"]["NONCE"] = base64.b64encode(received_nonce).decode()

    # Obter as chaves da sessão
    encryption_key = base64.b64decode(sessions[received_session_id]["KEYS"]["ENCRYPTION_KEY"])
    integrity_key = base64.b64decode(sessions[received_session_id]["KEYS"]["INTEGRITY_KEY"])

    # Desencriptar o payload
    decrypted_payload = json.loads(decrypt_data_AES_CBC(received_encrypted_payload, encryption_key, received_iv))
    
    # Serializar o payload e verificar se o HMAC é valido
    payload_bytes = json.dumps(decrypted_payload).encode()
    message = received_session_id.encode() + payload_bytes + received_iv + received_nonce
    calculated_hmac_signature = calculate_hmac(message, integrity_key)

    if calculated_hmac_signature != received_hmac_signature:
        return json.dumps({"Error": "HMAC not valid"}), 400
    
    # Obter os dados do payload
    organization_name = decrypted_payload["organization_name"]
    username = decrypted_payload["username"]
    document_name = decrypted_payload["document_name"]
    operation = decrypted_payload["operation"]
    role_to_modify = decrypted_payload["role"]
    permission = decrypted_payload["permission"]

    # Verificar se a organização existe
    if organization_name not in organizations:
        return json.dumps({"Error": "Organization doesn't exist"}), 400
    
    # Verificar se o username é válido
    if username not in organizations[organization_name]["SUBJECTS"]:
        return json.dumps({"Error": "Username doesn't exist"}), 400
    
    # Criar o document_handle: hash do nome do documento + nome da organização
    digest = hashes.Hash(hashes.SHA256())
    message = document_name.encode() + organization_name.encode()
    digest.update(message)
    document_handle = base64.b64encode(digest.finalize()).decode()

    # Verificar se o document_handle é válido (ou seja, se o document_name existe na organization)
    if document_handle not in documents:
        return json.dumps({"Error": "Document name doesn't exists in the organization"}), 400
    
    # Filtrar apenas as roles que estão ativas
    active_subject_roles = [role for role in sessions[received_session_id]["ROLES"] if organizations[organization_name]["ACL"][role]["STATUS"] == "ACTIVE"]

    # Verificar se tem a permissão necessária
    for role in active_subject_roles:
        if role in documents[document_handle]["ACL"] and "DOC_ACL" in documents[document_handle]["ACL"][role]:

            # Verificar se a operação que quer realizar é valida
            if operation != "+" and operation != "-":
                return json.dumps({"Error": "Invalid operation"})
            
            # Verificar se a permissão que o subject quer adicionar existe 
            if permission not in ["DOC_ACL", "DOC_READ", "DOC_DELETE"]:
                return json.dumps({"Error": "Permission does not exist"})
            
            # Verificar se a role que o subject está a tentar alterar na ACL do documento existe
            if role_to_modify not in organizations[organization_name]["ACL"]:
                return json.dumps({"Error": "Role to modify does not exist in this organization"})
            
            # Verificar se a entry para essa role já existe na ACL do documento
            # Se não existir, criar
            if role_to_modify in documents[document_handle]["ACL"]:
                if operation == "+":
                    documents[document_handle]["ACL"][role_to_modify].append(permission)
                elif operation == "-" and permission in documents[document_handle]["ACL"][role_to_modify]:
                    documents[document_handle]["ACL"][role_to_modify].remove(permission)

                # No caso em que o subject está a tentar remover a permissão de uma role que não tem essa permissão
                else:
                    return json.dumps({"Error": "Role to change does not have this permission in this document"})
            else:
                if operation == "+":
                    documents[document_handle]["ACL"][role_to_modify] = [permission]
                # No caso em que o subject está a tentar remover a permissão de uma role que não tem permissões
                elif operation == "-":
                    return json.dumps({"Error": "Role to change does not have this permission in this document"})
                

            return json.dumps({"status": "success", "message": "Document ACL updated successfully"}), 200
        
    return json.dumps({"Error": "Missing permissions to change document ACL"}), 400
# <----------------------------->


if __name__ == '__main__':
    app.run(debug=True)