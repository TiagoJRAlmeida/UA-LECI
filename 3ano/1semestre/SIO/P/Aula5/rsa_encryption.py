from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import sys

def rsa_encrypt(input_file: str, public_key_file: str, output_file: str):
    
    with open(input_file, 'rb') as ifile:
        message = ifile.read()
    
    with open(public_key_file, 'rb') as publickf:
        public_key_bytes= publickf.read()
        
    public_key = serialization.load_pem_public_key(public_key_bytes)
    ciphertext = public_key.encrypt(message, padding.PKCS1v15())
    
    with open(output_file, 'wb') as ofile:
        ofile.write(ciphertext)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 rsa_encryption.py <original_file> <public_key.pem> <output_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    public_key = sys.argv[2]
    output_file = sys.argv[3]

    rsa_encrypt(input_file, public_key, output_file)

#rsa_encrypt("input_file.txt", "encrypted_file.txt", "public_key.pem")