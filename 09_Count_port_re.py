import paramiko,time,re,socket
from datetime import datetime
now = datetime.now()
date_now = '%s-%s-%s'%(now.year,now.month,now.day)
time_now = '%s:%s:%s'%(now.hour,now.minute,now.second)
class Port_statistics(object):
    switch_with_tacacs_issue = []
    switch_not_reachable = []
    total_number_of_up_port = 0
    def __init__(self):
        self.ssh_login()
        self.summary()
    def ssh_login(self):
        self.iplist = open('/Users/MrJoe/NetDevOps/NetDevOps/files/lab9_iplist')
        self.number_of_switch = len(self.iplist.readlines())
        self.iplist.seek(0)
        for line in self.iplist.readlines():
            try:
                self.ip = line.strip()
                self.ssh_client = paramiko.SSHClient()
                self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh_client.connect(hostname=self.ip,username='python',password='Huawei@123',look_for_keys=False)
                print('\n---------You have login on----------',self.ip)
                self.command = self.ssh_client.invoke_shell()
                self.check_port_up()
            except paramiko.ssh_exception.AuthenticationException:
                print('\n---------TACACS is not working for " + self.ip + "-----------"')
                self.switch_with_tacacs_issue.append(self.ip)
            except socket.error:
                print('\n---------' + self.ip + 'is not reachable------------')
                self.switch_not_reachable.append(self.ip)
        self.iplist.close()
    def check_port_up(self):
        self.command.send('term len 0\n ')
        self.command.send('show ip int b | i up\n')
        time.sleep(1)
        output = self.command.recv(65535).decode('ascii')
        print(output)
        self.search_up_port = re.findall(r'Ethernet',output)
        self.number_of_up_port = len(self.search_up_port)
        print (self.ip + " has " + str(self.number_of_up_port) + " ports up.")
        self.total_number_of_up_port += self.number_of_up_port
    def summary(self):
        self.total_number_of_ports = self.number_of_switch * 48
        print ("\n")
        print ("There are totally " + str(self.total_number_of_ports) + " ports available in the network.")
        print (str(self.total_number_of_up_port) + " ports are currently up.")
        print ("Port up rate is %.2f%%" % (self.total_number_of_up_port / float(self.total_number_of_ports) * 100))
        print ('\nTACACS is not working for below switches: ')
        for i in self.switch_with_tacacs_issue:
            print (i)
        print ('\nBelow switches are not reachable: ')
        for i in self.switch_not_reachable:
            print (i)
        f = open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab9_'+date_now + ".txt", "a+")
        f.write('As of ' + date_now + " " + time_now)
        f.write("\n\nThere are totally " + str(self.total_number_of_ports) + " ports available in the network.")
        f.write("\n" + str(self.total_number_of_up_port) + " ports are currently up.")
        f.write("\nPort up rate is %.2f%%" % (self.total_number_of_up_port / float(self.total_number_of_ports) * 100))
        f.write("\n***************************************************************\n\n")
        f.close()
if __name__ == '__main__':
    script1_2 = Port_statistics()








