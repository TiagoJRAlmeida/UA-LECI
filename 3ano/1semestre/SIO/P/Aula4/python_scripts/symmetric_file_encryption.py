import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from symmetric_padding_PKCS7 import add_padding_PKCS7

def encrypt_file(file_in: str, file_out: str, pkey_file: str, IV_file: str = None):
    
    if IV_file == None:
        encryption_mode = 'ECB'
    else:
        encryption_mode = 'CBC'
        with open(IV_file, "rb") as IV_f:
            iv = IV_f.read()

    with open(pkey_file, "rb") as pkey_f:
        key = pkey_f.read()
    
    with open(file_in, 'rb') as f_in:
        file_data = f_in.read()
    
    padded_data = add_padding_PKCS7(file_data) 
    
    if encryption_mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    elif encryption_mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB())
    else:
        raise ValueError(f"Unsupported encryption mode: {encryption_mode}")
    
    encryptor = cipher.encryptor()
    
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
    with open(file_out, 'wb') as f_out:
        f_out.write(encrypted_data)

if __name__ == "__main__":
    if len(sys.argv) not in {4, 5}:
        print("Usage:")
        print("Option(1): python3 symmetric_file_enctryption.py <file_in> <file_out> <public_key>")
        print("Option(2): python3 symmetric_file_enctryption.py <file_in> <file_out> <public_key> <IV>")
        sys.exit(1)

    file_in = sys.argv[1]
    file_out = sys.argv[2]
    pkey = sys.argv[3]

    if len(sys.argv) == 4:
        encrypt_file(file_in, file_out, pkey)
    else:
        iv = sys.argv[4]
        encrypt_file(file_in, file_out, pkey, iv)