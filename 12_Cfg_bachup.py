import paramiko,time
from getpass import getpass
username = input('Username:')
password = getpass('Password:')
f = open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab12_cfg-backup/lab12_iplist','r')
for line in f.readlines():
    ipaddress = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ipaddress,username=username,password=password,look_for_keys=False)
    print('~~~~~~~~~~~😆成功登录USG-6000V😆~~~~~~~~~~~~~~'+ ipaddress)
    huawei_cmd = ssh_client.invoke_shell()
    huawei_cmd.send('tftp 10.1.1.1 put hda1:/vrpcfg.zip vrpcfg.zip\n')
    time.sleep(3)
    huawei_cmd.send('sa\n')
    huawei_cmd.send('y\n')
    #通过TFTP将FW1下hda1:/vrpcfg.zip拷贝到10.1.1.1的transfer目录中
    time.sleep(1)
    result = huawei_cmd.recv(65535)
    print(result.decode('ascii'))
f.close()
ssh_client.close()
