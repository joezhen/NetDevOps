import paramiko,re,time,getpass,socket,sys
username = input('Username：')
password = input('Password：')
#FW_upgraded = []
#FW_not_upgraded = []
#FW_with_HWtacacs_issue = []
#FW_not_reachable = []
login_fw_iplist = open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab10_iplist','r+')
for line in login_fw_iplist.readlines():
    #try:
        ip_address = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password,look_for_keys=False)
        print ("Successfully connect to ", ip_address)
        command = ssh_client.invoke_shell(width=30)
        command.send("display version av-sdb\n")
        time.sleep(0.5)
        command.send("display update status\n")
        time.sleep(0.5)
        command.send("display license\n")
        command.send("sys\n")
        command.send("update local av-sdb file  hda1:/av_h20020000_2021050800.zip\n")
        time.sleep(2)
        output = command.recv(65535).decode("ascii")
        print(output)
    #except paramiko.ssh_exception.AuthenticationException:
       # print ("TACACS is not working for " + ip_address + ".")
        #FW_with_HWtacacs_issue.append(ip_address)
    #except socket.error:
        #print (ip_address +  " is not reachable.")
        #FW_not_reachable.append(ip_address)
login_fw_iplist.close()
ssh_client.close









