from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_key(key_length: int, public_file: str, private_file: str):
    allowed_sizes = [1024, 2048, 3072, 4096]
    if key_length in allowed_sizes:
        private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,)
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
    
    
generate_key(1024, 'public_key.pem', 'private_key.pem')
