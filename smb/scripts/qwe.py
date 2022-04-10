from smb.SMBConnection import SMBConnection


userid = 'admin'
password = 'admin'
client_machine_name = 'Windows'
remote_machine_name = '192.168.193.129'
server_ip = '192.168.193.129'

conn = SMBConnection(userid, password, client_machine_name, remote_machine_name, use_ntlm_v2 = True, is_direct_tcp = True)
conn.connect(server_ip, 445)

filelist = conn.listPath('Documents', '/')

for x in filelist:
    print(x.filename,'  ', x.create_time)
