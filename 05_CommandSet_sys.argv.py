#!coding=utf-8
import sys,paramiko,time,getpass
username = input('Username：')
password = getpass.getpass('Password：')
Enable_password=getpass.getpass('Enable Password：')
file_iplist_huawei = sys.argv[1]
file_commandlist_huawei = sys.argv[2]
file_iplist_cisco = sys.argv[3]
file_commandlist_cisco = sys.argv[4]
Huawei_AR=open(file_iplist_huawei,'r')
Cisco_3725 = open(file_iplist_cisco, 'r')
for line in Huawei_AR.readlines():
    ip=line.strip()
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)
    print('😝😝😝😝😝😝😝😝😝😝-----You have successfully connected to',ip,'-----🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶')
    command=ssh_client.invoke_shell()
    Huawei_AR_command=open(file_commandlist_huawei,'r')
    Huawei_AR_command.seek(0)
    for line in Huawei_AR_command.readlines():
        command.send(line+'\n')
        time.sleep(5)
    Huawei_AR_command.close()
    output=command.recv(65535).decode('ascii')
    print(output)
Huawei_AR.close()
ssh_client.close()
for line in Cisco_3725.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
    print('😝😝😝😝😝😝😝😝😝😝-----You have successfully connected to',ip,'-----🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶')
    command = ssh_client.invoke_shell()
    command.send('enable\n')
    command.send(Enable_password+'\n')
    Cisco_3725_command = open(file_commandlist_cisco, 'r')
    Cisco_3725_command.seek(0)
    for line in Cisco_3725_command.readlines():
        command.send(line + '\n')
        time.sleep(2)
    Cisco_3725_command.close()
    output = command.recv(65535).decode('ascii')
    print(output)
Cisco_3725.close()
ssh_client.close()





