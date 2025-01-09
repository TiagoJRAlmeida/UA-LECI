from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend
import os
import sys

def generate_ecc_keypair(password: str, output_file: str):
    # Generate a private key using curve P-521
    private_key = ec.generate_private_key(ec.SECP521R1(), default_backend())
    
    # Derive a salt for password-based encryption
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    # Encrypt private key using provided password
    encrypted_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )
    
    # Generate the public key
    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # Write both private and public keys to the same file
    with open(output_file, 'wb') as f:
        f.write(b"-----BEGIN SALT-----\n")
        f.write(salt)
        f.write(b"\n-----END SALT-----\n")
        f.write(encrypted_private_key)
        f.write(public_key_pem)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python p256_gen.py <password> <output_file>")
        sys.exit(1)
    
    password = sys.argv[1]
    output_file = sys.argv[2]
    generate_ecc_keypair(password, output_file)
    print(f"Key pair saved to {output_file}")
