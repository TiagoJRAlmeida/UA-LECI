import os
import sys
import json
import requests
import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import hashes
import shutil
from auxiliary_functions import *


def rep_create_org(state, organization, username, name, email, public_key_file):
    # Abrir e carregar o conteúdo do arquivo JSON de chaves
    with open(public_key_file, 'r') as f:
        keys_file = json.load(f)
    
    payload = {
        "organization_name": organization,
        "manager_subject": [username, name, email, keys_file["PUBLIC_KEY"]],
    }

    # Enviar o payload criptografado para o servidor
    url = f"http://{state['REP_ADDRESS']}/organization/create"
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Organization created successfully")
        sys.exit(0)
    else:
        print(f"Error when creating organization: {response.status_code}\nError Message: {response.json().get("Error")}")
        sys.exit(-1)
    

def rep_list_orgs(state):
    url = f"http://{state['REP_ADDRESS']}/organization/list"
    response = requests.get(url)
    orgs = response.json()
    
    if response.status_code == 200:
        print("Operation successful")
        terminal_width = shutil.get_terminal_size().columns
        bar_size = int((terminal_width - len("Organizations") - 4) / 2)
        print("\n+" + ("-"*bar_size) + " Organizations " + ("-"*bar_size) + "+\n")

        if orgs == []:
            print('No current organizations')
            sys.exit(-1)

        for index, org_name in enumerate(orgs):
            print(f'Organization {index + 1}: {org_name}')

        print("\n+" + ("-" * (terminal_width-2)) + "+\n")

        sys.exit(0)
    else:
        print(f"Operation Error: {response.status_code}")
        sys.exit(-1)


def rep_create_session(state, organization, username, password, credentials_file, session_file):
    # Abrir e carregar o conteúdo do arquivo JSON de chaves
    with open(credentials_file, 'r') as f:
        keys_file = json.load(f)
    
    # Carregar a chave privada do cliente
    client_private_key = load_pem_private_key(
        base64.b64decode(keys_file["ENCRYPTED_PRIVATE_KEY"]),
        password=password.encode()
    )
    
    # Criar o payload
    payload = {
        "organization_name": organization,
        "username": username,
        "public_key": keys_file["PUBLIC_KEY"],
    }
    
    # Gerar uma chave simetrica aleatoria de 256 bits e dividir em duas
    new_symmetric_key = os.urandom(32)  # 256 bits
    new_encryption_key = new_symmetric_key[0:16]
    new_integrity_key = new_symmetric_key[16:]
    
    # Usamos a nova encryption_key para cifrar o payload
    encrypted_payload, iv = encrypt_data_AES_CBC(json.dumps(payload).encode(), new_encryption_key)

    # Carregar a chave publica do repositório
    rep_public_key_data = state["REP_PUB_KEY"]
    if isinstance(rep_public_key_data, str):
        rep_public_key_data = rep_public_key_data.encode('utf-8')
    rep_public_key = load_pem_public_key(rep_public_key_data)

    # Cifrar a nova chave (256bits) com a REP_PUBLIC_KEY
    encrypted_key = rep_public_key.encrypt(
        new_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Criar a assinatura (Serve para verificar que a chave veio da pessoa certa)
    encrypted_key_signature = client_private_key.sign(
        encrypted_key,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Calcular o HMAC (Serve para verificar que a chave não foi alterada)
    hmac_signature = calculate_hmac(encrypted_key, new_integrity_key)
    
    # Gerar um nonce (Numero de 128 bits aleatório)
    nonce = os.urandom(16)

    payload = {
        "encrypted_payload": base64.b64encode(encrypted_payload).decode(),
        "encrypted_key": base64.b64encode(encrypted_key).decode(),
        "hmac": base64.b64encode(hmac_signature).decode(),
        "nonce": base64.b64encode(nonce).decode(),
        "iv": base64.b64encode(iv).decode(),
        "signature": base64.b64encode(encrypted_key_signature).decode()
    }

    # Enviar chave ao repositório
    url = f"http://{state['REP_ADDRESS']}/session/create"
    response = requests.post(url, json=payload)

    # Se a sessão foi criada com sucesso, guarda os dados
    if response.status_code == 200:

        data = response.json()
        received_session_id = data["session_id"]
        received_expiry_time = data["expiry_time"] 

        session_data = {
            "SESSION_ID": received_session_id,
            "ORGANIZATION_NAME": organization,
            "USERNAME": username,
            "KEYS": {
                "ENCRYPTION_KEY": base64.b64encode(new_encryption_key).decode(),
                "INTEGRITY_KEY": base64.b64encode(new_integrity_key).decode(),
                "NONCE": base64.b64encode(nonce).decode()
            },
            "ROLES": [],
            "EXPIRITY_TIME": received_expiry_time,
        }

        with open(session_file, "w") as sf:
            json.dump(session_data, sf)

        print("Operation successful")
        sys.exit(0)
            
    else:
        print(f"Operation Error: {response.status_code}\nError Message: {response.json().get("Error")}")
        sys.exit(-1)


def rep_get_file(state, file_handle, output_file=None):
    # Definir o payload
    payload = {
        "file_handle": file_handle
    }

    url = f"http://{state['REP_ADDRESS']}/doc/get/file_by_handle"
    response = requests.post(url, json=payload)

    # Se encontrou o ficheiro
    if response.status_code == 200:
        print("File retrieved successfully")
        
        data = response.json()

        encrypted_file_content = base64.b64decode(data["encrypted_file_content"])

        # Se for passado um ficheiro como argumento, escrever nele
        if output_file:
            with open(output_file, "wb") as f:
                f.write(encrypted_file_content)
                sys.exit(0)

        # Caso contrario returnar o conteudo
        print(encrypted_file_content)
        return encrypted_file_content
    
    else:
        print(f"Error when getting file: {response.status_code}\nError Message: {response.json().get("Error")}")
        sys.exit(-1)