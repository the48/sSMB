from main.login.py import *
import platform
import os

# needs the login import

if 'Windows' in str(platform.platform()):
    os.system('net view \\kali') # add the IP of the server
else:
    os.system(f'smbclient -u {username} -p {password} \\localhost')

