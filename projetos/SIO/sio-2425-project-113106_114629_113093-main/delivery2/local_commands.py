import shutil
import sys
import json
import base64
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives import hashes

def rep_subject_credentials(password, credentials_file):
    # Gerar par de chaves RSA
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    public_key = private_key.public_key()

    # Obter chave privada criptografada em formato PEM
    encrypted_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

    # Obter chave pública em formato PEM
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Codificar em base64 para compatibilidade com JSON
    payload = {
        "ENCRYPTED_PRIVATE_KEY": base64.b64encode(encrypted_private_key).decode('utf-8'),
        "PUBLIC_KEY": base64.b64encode(public_key_bytes).decode('utf-8')
    }

    # Salvar no arquivo JSON
    with open(credentials_file, 'w') as f:
        json.dump(payload, f, indent=4)

    print(f"Chaves salvas no arquivo {credentials_file} com sucesso!")


def rep_decrypt_file(encrypted_file, metadata):
    
    if os.path.isfile(encrypted_file):
        with open(encrypted_file, 'rb') as f:
            encrypted_file = f.read()

    if os.path.isfile(metadata):
        with open(metadata, 'r') as f:
            metadata = f.read()

    try:
        metadata = json.loads(metadata)
    except json.JSONDecodeError:
        print("Error: Metadata is not a valid JSON file.")
        sys.exit(-1)
    
    # Obter a chave e iv dos metadados
    decrypted_key = base64.b64decode(metadata["key"])
    iv = base64.b64decode(metadata["iv"])

    # Desencriptar o ficheiro
    # Inicializar o AES-CBC com a chave e o IV recebido
    cipher = Cipher(algorithms.AES(decrypted_key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    # Decifrar a encrypted_file
    decrypted_padded_file = decryptor.update(encrypted_file) + decryptor.finalize()

    # Remover o padding com PKCS7
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_file = unpadder.update(decrypted_padded_file) + unpadder.finalize()

    # Transformar a decrypted_file no formato correto 
    decrypted_file = decrypted_file.decode()

    terminal_width = shutil.get_terminal_size().columns
    bar_size = int((terminal_width - len("File Content") - 4) / 2)
    print("\n+" + ("-" * bar_size) + " File Content " + ("-" * bar_size) + "+\n")
    print(decrypted_file)
    print("\n+" + ("-" * (terminal_width-2)) + "+\n")
    return decrypted_file

