import time
from netmiko import ConnectHandler,file_transfer
print('~~~~~~~~~~~~~~~~~~~~~demo1~Netmiko登录多台交换机(用户密码端口一致)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def NetmikoLogin_SAME_username_password_port():
    name = 0
    with open ('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab11_iplist') as f:
        for ip_adds in f.readlines():
            ip_adds.strip()
            name +=1
            connect = {
                  'device_type':'huawei',
                  'ip':ip_adds,
                  'username':'python',
                  'password':'Huawei@123'
            }
            with ConnectHandler(**connect) as conn:
               print(f'已经成功登录路由器：{ip_adds}')                     #format格式化输出
               print("已经成功登录路由器：{}".format(ip_adds))             #等同于上条print语句
               output_1 = conn.send_config_set('sys R'+str(name))      #设备命令
               output_2 = conn.save_config()                           #保存设备配置
               time.sleep(1)
               print(output_1,output_2)
#NetmikoLogin_SAME_username_password_port()          #执行demo1脚本函数
print('~~~~~~~~~~~~~~~~~~~~~demo2~Netmiko登录多台交换机(用户密码端口不一致)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def NetmikoLogin_NotSAME_username_password_port():
    import json
    with open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab11_FW.json') as F:
        FWs = json.load(F)           #json库load方法，返回值为列表，json.load()从文件中读取json字符串
        #print(type(FWs))            #FWs为列表，其元素为字典
    for fw in FWs:
        with ConnectHandler(**fw['connection']) as ssh_con:
            sysname = fw['name']
            print(f'成功登录防火墙：{sysname}')
            output = ssh_con.send_command('dis zone mgt')
            ssh_con.send_config_set('sys '+sysname)
            print(output,ssh_con.save_config() )
            time.sleep(1)
#NetmikoLogin_NotSAME_username_password_port()      #执行demo2脚本函数
print('~~~~~~~~~~~~~~~~~~~~~demo3~Netmiko配合Jinja2配置模板给设备做配置~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def Netmiko_cooperate_Jinja2():
   from jinja2 import Environment,FileSystemLoader
   router ={
            'device_type':'huawei',
            'ip':'10.1.1.11',
            'username':'python',
            'password':'Huawei@123'
   }
   loader = FileSystemLoader('/Users/MrJoe/NetDevOps/NetDevOps/files/templates')
   environment = Environment(loader=loader)
   tpl = environment.get_template('acl.conf.tpl')
   allow_ip = ['223.5.5.5 0']
   disallow_ip = ['8.8.8.8 0']
   output = tpl.render(allow_ip=allow_ip,disallow_ip=disallow_ip,interface='G0/0/1')
   with open('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab11-2_cfg.conf','w') as f:
       f.write(output)
   with ConnectHandler(**router) as conn:
       print('成功登陆路由器' + router['ip'])
       out = conn.send_config_from_file('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab11-2_cfg.conf')
       print(out)
#Netmiko_cooperate_Jinja2()                   #执行demo3脚本
print('~~~~~~~~~~~~~~~~~~~~~demo4~使用Netmiko向设备通过scp传送文件~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def Netmiko_scp_file():
    FW ={
        'device_type':'cisco_ios',              #华为设备不支持
        'ip':'10.1.1.14',
        'username':'python',
        'password':'Huawei@123',
        'secret':'Huawei@123'
    }
    with ConnectHandler(**FW) as FW_SCP_file:
        FW_SCP_file.enable()
        print('已经成功登录路由器：'+FW['ip'])
        #security_policy = FW_SCP_file.send_config_from_file('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab11-2_fw_cmd')
        #print(security_policy)
        file_tran = file_transfer(FW_SCP_file,
                      source_file = '/Volumes/存储/up/考证/03_HCIE-Security/培训资料_1121/实验/特征库/CSG_H50010002_2018073104.mod',
                      dest_file = 'CSG_H50010002_2018073104.mod',
                      file_system = 'flash:',
                      direction = 'put'
        )
        print(file_tran)
#Netmiko_scp_file()      #run一遍，如果dir有同名文件，结果会返回：'file_transferred': False
print('~~~~~~~~~~~~~~~~~~~~~~~~~~demo5~用Netmiko处理设备提示命令~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
def Netmiko_delete_flie():
    R1 = {
        'device_type':'cisco_ios',
        'ip':'10.1.1.14',
        'username':'python',
        'password':'Huawei@123',
        'secret':'Huawei@123'
    }
    with ConnectHandler(**R1) as R1_delete_file:
        print('成功登录路由器：'+R1['ip'])
        R1_delete_file.enable()
        print(R1_delete_file.find_prompt())      #打印当前视图
        output = R1_delete_file.send_command(command_string='delete flash0:CSG_H50010002_2018073104.mod',
           expect_string = r'Delete filename [CSG_H50010002_2018073104.mod]?',
           strip_prompt = False,    #strip_prompt和strip_command两个参数里放Fasle，目的让代码的print(output)输出的内容格式更好看
           strip_command = False)
        output += R1_delete_file.send_command(command_string="CSG_H50010002_2018073104.mod",
           expect_string=r"Delete flash0:CSG_H50010002_2018073104.mod?",
           strip_prompt=False,
           strip_command=False)
        output += R1_delete_file.send_command(command_string="y",
           expect_string=r"#",
           strip_prompt=False,
           strip_command=False)
        print(output)
Netmiko_delete_flie()




