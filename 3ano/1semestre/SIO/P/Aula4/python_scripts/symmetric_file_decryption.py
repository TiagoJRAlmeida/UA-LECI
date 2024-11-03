import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from symmetric_padding_PKCS7 import remove_padding_PKCS7 

def decrypt_file(file_in: str, file_out: str, public_key: str, iv: str = None):
    
    if iv == None:
        encryption_mode = 'ECB'
    else:
        encryption_mode = 'CBC'
        with open(iv, "rb") as IV_f:
            iv = IV_f.read()

    with open(public_key, "rb") as pkey_f:
        key = pkey_f.read()
    
    with open(file_in, 'rb') as f_in:
        file_data = f_in.read()
        
    if encryption_mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    elif encryption_mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB())
    else:
        raise ValueError(f"Unsupported encryption mode: {encryption_mode}")
    
    decryptor = cipher.decryptor()
    
    decrypted_data = decryptor.update(file_data) + decryptor.finalize()
    
    unpadded_decrypted_data = remove_padding_PKCS7(decrypted_data) 

    with open(file_out, 'wb') as f_out:
        f_out.write(unpadded_decrypted_data)


if __name__ == "__main__":
    if len(sys.argv) not in {4, 5}:
        print("Usage:")
        print("Option(1): python3 symmetric_file_dectryption.py <file_in> <file_out> <public_key>")
        print("Option(2): python3 symmetric_file_dectryption.py <file_in> <file_out> <public_key> <IV>")
        sys.exit(1)

    file_in = sys.argv[1]
    file_out = sys.argv[2]
    pkey = sys.argv[3]

    if len(sys.argv) == 4:
        decrypt_file(file_in, file_out, pkey)
    else:
        iv = sys.argv[4]
        decrypt_file(file_in, file_out, pkey, iv)
