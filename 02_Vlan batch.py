#!/usr/bin/env python3
import paramiko
import time
import getpass                           #引入paramiko、time、getpass模块
Username=input('Username：')             #调用交互式input函数，赋值给变量Username
Password=getpass.getpass('Password：')   #调用getpass函数，实现密码输入隐藏显示
for m in range(11,16):                   #for in 对登录的交换机做+1的外层循环
    ip= '10.1.1.' + str(m)
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=Username, password=Password,look_for_keys=False)
    print('You have logined on: ', ip)
    command=ssh_client.invoke_shell()
    command.send('sys\n')
    command.send('sysname '+'AR'+str(m-10)+'\n')
    for n in range(10,21):                #for in创建vlan10-20的内层循环
        print('Creating vlan'+str(n))
        command.send('vlan '+str(n)+'\n')
        command.send('name Python_Vlan'+str(n)+'\n')
        time.sleep(0.5)
    command.send('quit\n'*2)
    command.send('sa\n')
    command.send('y\n')
    time.sleep(2)
    output=command.recv(65535).decode('ascii')        #打印输出显示，并以ascii显示，避免二进制乱码显示
    print(output,'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~please check configuration！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    time.sleep(5)
ssh_client.close()











