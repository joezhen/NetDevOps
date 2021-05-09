print('-----------------------------------自定义模块-----------------------------------------------')
#模块：将自定义函数写入脚本文件中，然后作为模块import导入重复使用，脚本名即模块名；分为带自定义函数模块和不带自定义函数模块
import script1    ##脚本1必须和当前py同一个文件目录
print('这是不带函数的脚本2')
import script1_def             #脚本1中定义了三个函数test、fun1_sum、fun2_count，则调用时写法：模块名.函数名(参数)
print('这是带函数的脚本2')
script1_def.test()            #打印test函数的hello
script1_def.fun1_sum(3,4)     #打印fun1_sum函数3+4=7
script1_def.fun2_count(5)     #打印fun2_count函数5的5次方=3125
print('----------------------------内建模块/三方模块(第三方库)----------------------------------------')
#python自带内建模块,import即可使用，以能实现ping命令功能的os模块为例，其他还有subprocess和pythonping
import os                           #os模块用来与运行代码的主机操作系统交互命令
hostname = 'www.huawei.com'
resource = os.system('ping -c 1 '+hostname)   #注意空格
                                              #调用os模块的system方法，返回值为一个整数：0表示目标可达，非0不可达
if resource ==0:
    print(hostname,'is reachable')
else:
    print(hostname,'is not reachable')
#第三方模块：pip2、pip3、pip3.8安装第三方模块，比如用于ssh登录网络设备的paramiko和netmiko
import  paramiko,netmiko
print('----------------------------------from...import ...------------------------------------------')
#from 模块名 import 函数名：省去调用模块函数时必须加上模块名
from script1_def import fun3_division       #导入模块的fun3方法
print('这是带函数的脚本2')
fun3_division(250,5)                        #方法fun3_division为m/n求商，直接打印50
print('----------------------------------__name__ == __main__------------------------------------------')
#__name__ == '__main__': 作为判断语句，带双下划线的变量叫作内置变量，如__name__;
#！！！所有写在该判断语句下的代码都将不会在该脚本被其他脚本用做模块import时被执行
import script1_if_main
print('这是引用了if main语句的脚本2')      #不打印script1_if_main中if main判断语句下的'在__name__语句内'









