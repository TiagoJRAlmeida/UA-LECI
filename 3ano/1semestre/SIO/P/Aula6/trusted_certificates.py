import os
from validity_check import valid
from cryptography import x509


def trusted(dir_name: str) -> dict:
    """This function reads all the certificates saved in the given directory, returning them in a dictionary
    
    Args:
        dir_name (str): directory name where the certificates are saved

    Returns:
        dict: dictionary with keys as the certificates subjects and as values the corresponding certificates
    """
    result = {}          
                
    # Code with the necessary logic
    objects = os.scandir(dir_name)

    for obj in objects:
        if obj.name.endswith(".pem"):
            with open(obj.path, "rb") as fcert:
                cert = x509.load_pem_x509_certificate(fcert.read())
                if valid(cert):
                    result[cert.subject] = cert


    return result

def main():
    trust_certs = trusted("/etc/ssl/certs")
    print(f"{len(trust_certs)} valid trusted certificates found")
            

if __name__ == "__main__":
    main()
