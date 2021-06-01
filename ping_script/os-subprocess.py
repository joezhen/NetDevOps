import os,subprocess
hostname = open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab0_ping_hostname')
for line in hostname.readlines():
    ip = line.strip()
#print('😆~~~~~~~~~~~☺️~~~~~~~~~~~~~ping-demo1：os.system~~~~~~~~~~~☺️~~~~~~~~~~~~~😆')
    #def os_ping():
    response = os.system('ping -c 2 '+ ip)
    if response == 0:
       print('\n'+ ip +' network is okay'+'\n')
    else:
       print('\n'+ ip + ' is not reachable'+'\n')
#print('😆~~~~~~~~~~~☺️~~~~~~~~~~~~~ping-demo2：subprocess~~~~~~~~~~~~~☺️~~~~~~~~~~~😆')
    #def subprocess_ping():
    ping_result = subprocess.call(['ping','-c','2',ip])
    reachable_iplist = []
    timeout_iplist = []
    if ping_result == 0:
       reachable_iplist.append(ip)
    else:
       timeout_iplist.append(ip)
    print(reachable_iplist)
    print(timeout_iplist)
#print('😆~~~~~~~~~~~☺️~~~~~~~~~~~~~ping-demo3：pythonping~~~~~~~~~~~~~☺️~~~~~~~~~~~😆')
import pythonping
