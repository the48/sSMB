from smb.SMBConnection import SMBConnection
from cryptography.fernet import Fernet
from simple_term_menu import TerminalMenu
from art import tprint

import platform
import hashlib
import argparse
import time
import os


# Encryption Section

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
    with open('downloads/' + fileName, 'rb') as enc_doc:
        encrypted = enc_doc.read()

    decrypted = fernet.decrypt(encrypted)

    with open('downloads/' + fileName, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


# Hashing Section
def make_md5(fileName):
    hash_md5 = hashlib.md5()
    with open(fileName, "rb") as f:
        for x in iter(lambda: f.read(4096), b""):
            hash_md5.update(x)
    print(hash_md5.hexdigest())


# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', required=True)
parser.add_argument('-p', '--password', required=False)

args = parser.parse_args()

userID = args.username
password = args.password

client_machine_name = 'Windows'

server_name = '192.168.193.129'
server_ip = 'kali'

domain_name = 'WORKGROUP'

conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)

conn.connect(server_ip, 445)

# Clear screen
os.system('cls||clear')
time.sleep(1)
print('[!] Connected Successfully!')

# Enumerate Shares
def getShares():
    if "Windows" in str(platform.platform()):
        os.system("net view \\kali")
    else:
        os.system(f'smbclient -L //{server_ip} -U {username} -P {password}')


# Send File
def sendFile(fileName):
    try:
        with open(fileName, 'rb') as t:
            # Create hash
            hash_md5 = hashlib.md5()
            for x in iter(lambda: t.read(4096), b""):
                hash_md5.update(x)
            #print(hash_md5.hexdigest())
            
            with open(fileName + '_md5', 'w+') as x:
                x.write(hash_md5.hexdigest())
            
            # Encrypt file
            encrypt_file(fileName)

            # Send file
            with open(fileName, 'rb') as f:
                conn.storeFile('Documents', fileName, f)

            # Send hash
            with open(fileName + '_md5', 'rb') as c:
                conn.storeFile('Documents', fileName + '_md5', c)

    except Exception as e:
        print(f"Error: {e}")



def getFile(fileName):
    try:
        with open('downloads/' + fileName, 'wb+') as f:
            conn.retrieveFile('Documents', fileName, f)
        decrypt_file(fileName)
        
        #with open(fileName + '_md5') as m:
        #    conn.retrieveFile('Documents', fileName, m)


        #if 'Linux' in str(platform.platform()):
        #    os.system('md5sum ' + fileName + '_md5')
    except Exception as e:
        print(f'[!] Error: {e}')


# Key Backup
def key_backup():
    with open('./downloads/key.key', 'wb+') as k:
        conn.retrieveFile('Key', 'key.bak', k)


def report_file():
    time.sleep(.3)
    print('[!] Still under development!')

def authentication():
    time.sleep(.3)
    print('[!] Report issue to Administrator')

def other():
    time.sleep(.3)
    print('[!] Still under development!')


#make_key()
#sendFile('notes')
#getFile('notes')


tprint('S-SMB')

# Menu Interface
menu = ['[1] Send file', '[2] Get file', '[3] Troubleshooting', '[q] Quit']
sub_menu = ['[1] Request key', '[2] Authentication issue', '[3] Report file integrity', '[4] Other', '[b] Back']
exit = True


while exit:
    choice = menu[TerminalMenu(menu).show()]

    if choice == '[1] Send file':
        local_doc = input('Enter the path to the file: ')
        sendFile(local_doc)
        time.sleep(.4)
        print('[!] File encrypted and uploaded')
    elif choice == '[2] Get file':
        remote_doc = input('Enter the name of the file: ')
        getFile(remote_doc)
        time.sleep(.4)
        print('[!] File decryptred and downloaded')

    elif choice == '[3] Troubleshooting':
        sub_menu_state = True
        while sub_menu_state:
            choice = sub_menu[TerminalMenu(sub_menu, title = 'Troubleshooting').show()]

            if choice == '[1] Request key':
                key_backup()
            elif choice == '[2] Authentication issue':
                authentication()
            elif choice == '[3] Report file integrity':
                report_file()
            elif choice == '[4] Other':
                other()
            elif choice == '[b] Back':
                time.sleep(.3)
                os.system('cls||clear')
                sub_menu_state = False

    elif choice == '[q] Quit':
        exit = False


