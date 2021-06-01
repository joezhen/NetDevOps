from netmiko import ConnectHandler           #netmiko的ssh模块，相当于paramiko的ssh_client
class cisco_ASA:
      ASA = {'device_type':'cisco_ios',      #device_type的键值必须为支持的型号，不能自定义
      'ip':'10.1.1.60',
      'username':'admin',
      'password':'Huawei@123',               #用户密码
      'secret':'Huawei@123'                  #enable密码
      }
      cisco_connect = ConnectHandler(**ASA)     #调用ConnectHandler子模块，把字典S2作为**关键字参数，赋值给connect变量
      print('已经成功登录交换机:'+ASA['ip'])       #字典索引，调用键值
      current_view = cisco_connect.find_prompt()
      print(current_view)
      cisco_connect.enable()                         #进入enable模式
      config_commands = ['int e1',
                         'no sh',
                         'ip add 2.2.2.2 255.255.255.0']
      output = cisco_connect.send_config_set(config_commands)
      print(output)
      result = cisco_connect.send_command('sh int e1')
      print(result)
      cisco_connect.disconnect()
class huawei_USG:
      USG = {'device_type':'huawei',
             'ip':'10.1.1.21',
             'username':'python',
             'password':'Huawei@123'
             }
      huawei_connect = ConnectHandler(**USG)
      print('已经成功登录交换机:'+USG['ip'])
      current_view = huawei_connect.find_prompt()
      print(current_view)
      config_commands = ['int e1',
                         'ip add 2.2.2.2 255.255.255.0']
      output = huawei_connect.send_config_set(config_commands)
      print(output)
      result = huawei_connect.send_command('dis ip int br')
      print(result)
      huawei_connect.disconnect()





