import time
print('----------------------------demo1~ssh交互式登录--------------------------------')
import getpass,pprint,textfsm
from pprint import pprint
from netmiko import ConnectHandler
Huawei_USG = {
    'device_type':'huawei',
    'ip':'10.1.1.21',
    'username':input('请输入用户名：'),                    #明文交互式input方法
    'password':getpass.getpass('请输入密码：'),            #密文交互式getpass方法
    #'secret':getpass.getpass('请输入密码：')
}
with ConnectHandler(**Huawei_USG) as connect:
    commands = ['int lo1','ip add 33.33.33.33 24','desc Lab11_Netmiko']
    #with..as语句：context manager调用sw1字典关键字参数**作为ConnetHandler的参数
    #可以在脚本运行完毕后自动帮助我们关闭SSH会话
    #最后，赋值给connect
    print('已经成功登录华为防火墙: '+Huawei_USG['ip'])
    #connect.enable()      #进入enable模式
    current_view = connect.find_prompt()     #打印当前视图
    print(current_view)
    print('----------------------------demo2~设备下发配置--------------------------------')
    output = connect.send_config_set(commands)
    print(output)
    output = connect.send_config_from_file('/Users/MrJoe/NetDevOps/NetDevOps/files/Lab11_config')
    print(output)
    output = connect.send_command('sa')
    print(output)
    output = connect.send_command('dis ip int bri')
    print(output)
    print('----------------------------demo3~Textfsm+pprint回显JSON格式输出--------------------------------')
    output = connect.send_command('dis interface',use_textfsm = True)   ##使用textfsm下
    #time.sleep(1)
    pprint(output)
    print('----------------------------demo4~Genie+pprint回显JSON格式输出--------------------------------')
    output = connect.send_command('dis interface',use_genie = True)     ##使用textfsm下
    pprint(output)
    
