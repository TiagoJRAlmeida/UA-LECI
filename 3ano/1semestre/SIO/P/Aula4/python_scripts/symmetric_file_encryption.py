import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from symmetric_padding_PKCS7 import add_padding_PKCS7, remove_padding_PKCS7
from symmetric_key_generation import generate_key_iv_from_password

def encrypt_file(file_in: str, file_out: str, encryption_mode: str, password: str):
    salt = os.urandom(16)
    key, iv = generate_key_iv_from_password(password, salt)
    
    with open(file_in, 'rb') as f_in:
        file_data = f_in.read()
    
    padded_data = add_padding_PKCS7(file_data) 
    
    # Choose encryption mode
    if encryption_mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    elif encryption_mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    else:
        raise ValueError(f"Unsupported encryption mode: {encryption_mode}")
    
    encryptor = cipher.encryptor()
    
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    encoded_salt = base64.b64encode(salt).decode('utf-8')
    encoded_iv = base64.b64encode(iv).decode('utf-8') if encryption_mode == 'CBC' else ''
    encoded_encrypted_data = base64.b64encode(encrypted_data).decode('utf-8')
    
    with open(file_out, 'w') as f_out:
        f_out.write(f"{encoded_salt}\n{encoded_iv}\n{encoded_encrypted_data}\n")

password = "your_secure_password"
encrypt_file('input.txt', 'output.txt', 'CBC', password)
