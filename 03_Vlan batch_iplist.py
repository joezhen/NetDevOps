#!usr/bin/env python3
import paramiko
import time
import getpass
Username=input('Username：')
Password=getpass.getpass('Password：')
ip=open('/Users/MrJoe/NetDevOps/NetDevOps/files/lab3_iplist.txt','r')
for line in ip.readlines():
    mgt_ip=line.strip()
    Gi01_ip='192.168.1.'+str(list(mgt_ip)[7])+str(list(mgt_ip)[8])
    SSH_Client=paramiko.SSHClient()
    SSH_Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSH_Client.connect(hostname=mgt_ip,username=Username,password=Password,look_for_keys=False)
    print('Congratulation！You have login on '+mgt_ip)
    remote_connection=SSH_Client.invoke_shell()
    remote_connection.send('sys\n')
    remote_connection.send('int Gi0/0/1\n')
    remote_connection.send('ip add ')
    remote_connection.send(Gi01_ip)
    remote_connection.send(' 24\n')
    remote_connection.send('undo ospf net \n')
    remote_connection.send('ospf 1 router-id ')
    remote_connection.send(mgt_ip)
    remote_connection.send('\n')
    remote_connection.send('area 0.0.0.0\n')
    remote_connection.send('network 192.168.1.0 0.0.0.255\n')
    remote_connection.send('qu\n'*2)
    remote_connection.send('sa\n')
    remote_connection.send('y\n')
    time.sleep(5)
    output=remote_connection.recv(65535).decode('ASCII')
    print (output)
ip.close()
SSH_Client.close




