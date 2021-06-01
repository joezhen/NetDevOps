#!/usr/bin/env python3
import paramiko
import time           #导入库：paramiko、time
ipaddress='10.1.1.21'
manageuser='python'
password='Huawei@123'
ssh_client=paramiko.SSHClient()       #调用paramiko的sshclient方法
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())     #paramiko接受来自sshserver的public key，默认为拒绝
ssh_client.connect(hostname=ipaddress,username=manageuser,password=password,look_for_keys=False)   #调用connect函数
print('Congratulation！You have login on '+ipaddress)
Huawei_command=ssh_client.invoke_shell()      #调用invoke_shell方法，使其可以传入cli参数
Huawei_command.send('sys\n')
Huawei_command.send('sysname Lab1_FW1\n')
Huawei_command.send('interface Gi0/0/0\n')
Huawei_command.send('ip address 22.22.22.22 24\n')
Huawei_command.send('s p p\n')
Huawei_command.send('quit\n'*2)      ##Firewall执行两次quit
Huawei_command.send('save\n')
Huawei_command.send('y\n')
time.sleep(1)                      #系统稍候1s执行后续语句
output=Huawei_command.recv(65535)     #调用recv方法[截屏]运行script后所有输出记录
print(output.decode("ascii"))           #输出采用asci编码，避免回显为字符串显示
ssh_client.close()      #退出ssh








