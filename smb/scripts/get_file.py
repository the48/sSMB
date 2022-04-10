from login import *
from enc.py import decrypt_file
# import the decrypt thing
# key will be stored on server




def getFile(fileName, path):
    try:
        with open(fileName, 'wb') as f:
            conn.retrieveFile(path, fileName, f)
        # decrypt it
        # grab its md5sum
        # run md5 test
    except Exception as e:
        print(f'[!] Error: {e}')

    enc.decrypt_file(fileName)
    print('File decrypted')
