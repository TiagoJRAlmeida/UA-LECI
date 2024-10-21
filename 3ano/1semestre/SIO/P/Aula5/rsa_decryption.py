from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def rsa_decrypt(encrypted_file: str, output_file: str, private_key_file: str):
    
    with open(encrypted_file, 'rb') as efile:
        cyphertext = efile.read()
    
    with open(private_key_file, 'rb') as privatef:
        private_key_bytes= privatef.read()
        
    private_key = serialization.load_pem_private_key(private_key_bytes, password=None,)
    ciphertext = private_key.decrypt(cyphertext, padding.PKCS1v15())
    
    with open(output_file, 'wb') as ofile:
        ofile.write(ciphertext)
        
rsa_decrypt("encrypted_file.txt", "decrypted_file.txt", "private_key.pem")