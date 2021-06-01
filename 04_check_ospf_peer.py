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
    check_ospf_peer=SSH_Client.invoke_shell()
    check_ospf_peer.send('dis ospf p b\n')
    time.sleep(1)
    ospf_peer=check_ospf_peer.recv(65535).decode('ASCII')
    print(ospf_peer)
ip.close()
SSH_Client.close()
