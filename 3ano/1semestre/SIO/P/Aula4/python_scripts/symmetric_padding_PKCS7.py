from cryptography.hazmat.primitives import padding

def add_padding_PKCS7(data):
    padder = padding.PKCS7(128).padder()
    if type(data) != bytes:
        data = data.encode()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data


def remove_padding_PKCS7(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    if type(padded_data) != bytes:
        padded_data = padded_data.encode()
    data = unpadder.update(padded_data)
    data += unpadder.finalize()
    return data


def test(data):
    print("-"*50)
    print(f"Original text: {data}")
    padded_data = add_padding_PKCS7(data)
    print(f"Padded text: {padded_data}")
    unpadded_data = remove_padding_PKCS7(padded_data)
    print(f"Unpadded text: {unpadded_data}")
    print("-"*50)
    
# data = "Hello World!"
# test(data)