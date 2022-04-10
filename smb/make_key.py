from cryptography.fernet import Fernet


key = Fernet.generate_key()

def make_key():
    with open('key.key', 'wb') as keyFile:
        keyFile.write(key)


make_key()
