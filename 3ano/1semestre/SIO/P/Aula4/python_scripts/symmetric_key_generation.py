import os
from hashlib import pbkdf2_hmac

def generate_key_iv_from_password(password: str, salt: bytes, iterations: int = 100000) -> tuple:
    key_iv = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=32)
    
    key = key_iv[:16]
    iv = key_iv[16:]
    
    return key, iv

def test():
    password = "1234"
    salt = os.urandom(16)  # Random 128-bit salt

    # Generate key and IV
    key, iv = generate_key_iv_from_password(password, salt)

    print(key, iv)
    
#test()
