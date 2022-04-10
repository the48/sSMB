from cryptography.fernet import Fernet

key = Fernet.generate_key()

def make_key():
    with open('key.key', 'wb') as keyFile:
        keyFile.write(key)


with open('key.key', 'rb') as keyFile:
    asd = keyFile.read()
    fernet = Fernet(asd)


def encrypt_file(fileName):
    with open(fileName, 'rb') as doc:
        OG_doc = doc.read()

    encrypted_doc = fernet.encrypt(OG_doc)

    with open(fileName, 'wb') as enc_doc:
        enc_doc.write(encrypted_doc)



def decrypt_file(fileName):
    with open(fileName, 'rb') as enc_doc:
        encrypted = enc_doc.read()

    decrypted = fernet.decrypt(encrypted)

    with open(fileName, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)



#make_key()
#load_key()
#encrypt_file('notes')
decrypt_file('notes')
