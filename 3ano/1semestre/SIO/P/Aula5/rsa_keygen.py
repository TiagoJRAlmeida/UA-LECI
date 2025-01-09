from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

def rsa_generate_key(public_file: str, private_file: str, key_length: int):
    allowed_sizes = [1024, 2048, 3072, 4096]
    if key_length in allowed_sizes:
        private_key = rsa.generate_private_key(public_exponent=65537,key_size=key_length,)
        public_key = private_key.public_key()
        private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()) 
        public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
        
        with open(public_file, 'wb') as publicf:
            publicf.write(public_key_pem)
            
        with open(private_file, 'wb') as privatef:
            privatef.write(private_key_pem)
            
    else:
        print('\nSelect a valid key size.')
        return
    
    
if __name__ == "__main__":
    possible_values = [1024, 2048, 3072, 4096]

    if len(sys.argv) != 4 or sys.argv[3].isnumeric == False or int(sys.argv[3]) not in possible_values:
        print("Usage: python3 keygen.py <public_file.pem> <private_file.pem> <key_length>")
        print("Allowed sizes: 1024, 2048, 3072 or 4096")
        sys.exit(1)
    
    public_file = sys.argv[1]
    private_file = sys.argv[2]
    key_length = int(sys.argv[3])

    rsa_generate_key(public_file, private_file, key_length)