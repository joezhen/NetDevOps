#实验目的：避免因为个别设备登录异常导致脚本无法继续运行
# 1. 手动shutdown R2端口导致python抛出连接失败异常（TimeoutError: [Errno 60] Operation timed out）
# 2. 手动修改R4 ssh用户密码导致python抛出认证失败异常（paramiko.ssh_exception.SSHException: Unable to open channel.）
import paramiko,time,socket,sys,getpass
Username=input('Username：')
Password=getpass.getpass('Password：')
ip_file=sys.argv[1]
#「argv」是「argument variable」参数变量的简写形式，这个变量返回的是一个列表；

# argv[0] 一般是被调用的脚本的文件名或全路径，从argv[1]开始就是传入的数据了
#sys.argv[1]表示传入的第一个文件数据即Lab6_iplist
command_file=sys.argv[2]
#sys.argv[2]表示传入的第二个文件数据即Lab6_commandlist
switch_timeout_error=[]
switch_authentication_error=[]
iplist=open(ip_file,'r')
for line in iplist.readlines():
    try:
        ip=line.strip()
        ssh_client=paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(hostname=ip,username=Username,password=Password,look_for_keys=False)
        print('👧👧👧👧👧👧👧👧👧👧--------You have logined in',ip,'--------👩👩👩👩👩👩👩👩👩👩')
        command=ssh_client.invoke_shell()
        cmdlist=open(command_file,'r')
        cmdlist.seek(0)
        for line in cmdlist.readlines():
            command.send(line+'\n')
        time.sleep(2)
        cmdlist.close()
        outbound=command.recv(65535).decode('ascii')
        print(outbound)
    except socket.error:                             #匹配（TimeoutError: [Errno 60] Operation timed out）异常
        print('SSH connected time out '+ip+'!')
        switch_timeout_error.append(ip)
    except paramiko.ssh_exception.SSHException:          #匹配paramiko.ssh_exception.SSHException异常
        print('User Authenticationn failed for '+ip+'!')
        switch_authentication_error.append(ip)
iplist.close()
ssh_client.close
print('💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣Warnning!!!💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣')
print ('Below switches User authentication failed for :')
for i in switch_authentication_error :
    print (i)
print ('Below switches are not reachable: ')
for i in switch_timeout_error:
    print (i)










