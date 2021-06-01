from pythonping import ping
import os
if os.path.exists('/Users/MrJoe/NetDevOps/NetDevOps/files/script_file/reachable_ip.txt'):
    os.remove('/Users/MrJoe/NetDevOps/NetDevOps/files/script_file/reachable_ip.txt')
if os.path.exists('/Users/MrJoe/NetDevOps/NetDevOps/files/script_file/not_reachable_ip.txt'):
    os.remove('/Users/MrJoe/NetDevOps/NetDevOps/files/script_file/not_reachable_ip.txt')
third_octet = range(1,2)
last_octet = range(11,14)
normal = open('/Users/MrJoe/NetDevOps/NetDevOps/files/script_file/reachable_ip.txt','a')
abnormal = open('/Users/MrJoe/NetDevOps/NetDevOps/files/script_file/not_reachable_ip.txt','a')
for ip_3 in third_octet:
    for ip_4 in  last_octet:
        ip = '10.1.' + str(ip_3) + '.' + str(ip_4)
        ping_result = ping(ip)
        if 'Reply' in str(ping_result):       #注意Reply首字母必须大写，否则返回结果不正常。
            print (ip + ' is reachable.')
            normal.write(ip + '\n')
        else:
            print(ip + ' is not reachable!')
            abnormal.write(ip + '\n')
normal.close()
abnormal.close()

