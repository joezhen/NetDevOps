print('😆😆😆😆😆😆😆😆😆😆😆😆😆😆---demo1~test~ssh---😆😆😆😆😆😆😆😆😆😆😆😆😆😆')
from netmiko import ConnectHandler
class test_ssh:
    ip=open('/Users/MrJoe/NetDevOps/NetDevOps/files/lab8_iplist','r')
    for line in ip.readlines():
        mgt_ip=line.strip()
        ip.seek(0,0)
        Lab8_R = {'device_type':'cisco_ios',
                  'ip':mgt_ip,
                  'username':'python',
                  'password':'Huawei@123',
                  'secret':'Huawei@123'
                  }
        cisco_connect=ConnectHandler(**Lab8_R)
        print('已经成功登录交换机:'+Lab8_R['ip'])
        cisco_connect.enable()
        current_view = cisco_connect.find_prompt()
        print(current_view)
        test_cmd = cisco_connect.send_command('sh ip int b | i up ')
        print(test_cmd)
print('😆😆😆😆😆😆😆😆😆😆😆😆😆😆---demo2~test~alive~host---😆😆😆😆😆😆😆😆😆😆😆😆😆😆')
import paramiko
import time
import subprocess    #subprocess模块为ping模块
import os
class ping(object):
    third_object=range(1,6)
    fourth_object=range(11,120)
    def __init__(self):
        self.ping()
    def ping(self):
        self.remove_last_reachable_ip_file_exist()        #调用了下方的方法
        for IP_3 in self.third_object:
            for IP_4 in self.fourth_object:
                self.ip = '10.1.'+str(IP_3)+'.'+str(IP_4)
                self.ping_result = subprocess.call(['ping','-c','1','-i','1',self.ip])
                self.open_ip_record_file()
                self.check_ping_result()
        self.f.close()
    def open_ip_record_file(self):
        self.f = open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab8_reachable_ip.txt','a')
    def check_ping_result(self):
        if self.ping_result == 0:                     #subprocess方法返回0表示目标ip可达，1和2不可达
            self.f.write(self.ip + '\n')
    def remove_last_reachable_ip_file_exist(self):
        if os.path.exists('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab8_reachable_ip.txt'):
            #判断文件是否存在，保证每次运行脚本得到的内容都是最新且不冗余
           os.remove('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab8_reachable_ip.txt')
if __name__ == '__main__':
    script1_1 = ping()











