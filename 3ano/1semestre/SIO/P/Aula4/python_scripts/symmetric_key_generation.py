import os
import sys
from hashlib import pbkdf2_hmac

def generate_key_iv_from_password(password: str, salt: bytes = None, iterations: int = 100000, pkey_file: str = None, IV_file: str = None) -> tuple:
    
    if salt is None:
        salt = os.urandom(16)

    key_iv = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=32)
    
    key = key_iv[:16]
    iv = key_iv[16:]
    
    if pkey_file is not None:
        with open(pkey_file, "w") as pkey_f:
            pkey_f.write(key.hex())

    if IV_file is not None:
        with open(IV_file, "w") as IV_f:
            IV_f.write(iv.hex())

    return key, iv, salt
    
if __name__ == "__main__":

    if len(sys.argv) not in  {2, 4}:
        print("Usage:") 
        print("Option(1): python3 symmetric_key_generation.py <password>")
        print("Option(2): python3 symmetric_key_generation.py <password> <public_key_file> <IV_file>")
        sys.exit(1)

    password = str(sys.argv[1])
    if len(sys.argv) == 4:
        pkey_f = sys.argv[2]
        iv_f = sys.argv[3]
        key, iv, salt = generate_key_iv_from_password(password, pkey_file=pkey_f, IV_file=iv_f)
    else:
        key, iv, salt = generate_key_iv_from_password(password)

    print("\n+"+("-"*60)+"+")
    print("\tKey:", key.hex())
    print("\tIV:", iv.hex())
    print("\tSalt:", salt.hex())
    print("+"+("-"*60)+"+")