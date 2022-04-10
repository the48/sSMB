from smb.SMBConnection import SMBConnection
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', required = True)
parser.add_argument('-p', '--password', required = True)
args = parser.parse_args()

username = args.username
password = args.password

client_machine = 'Windows'

server_name = 'localhost'
server_ip = '127.0.0.1'

domain_name = 'WORKGROUP'

conn = SMBConnection(username, password, client_machine, server_name, domain = domain_name, use_ntlm_v2 = True, is_direct_tcp = True)
conn.connect(server_ip, 445)
