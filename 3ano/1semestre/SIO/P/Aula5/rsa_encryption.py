from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def rsa_encrypt(input_file: str, output_file: str, public_key_file: str):
    
    with open(input_file, 'rb') as ifile:
        message = ifile.read()
    
    with open(public_key_file, 'rb') as publickf:
        public_key_bytes= publickf.read()
        
    public_key = serialization.load_pem_public_key(public_key_bytes)
    ciphertext = public_key.encrypt(message, padding.PKCS1v15())
    
    with open(output_file, 'wb') as ofile:
        ofile.write(ciphertext)
        
rsa_encrypt("input_file.txt", "encrypted_file.txt", "public_key.pem")