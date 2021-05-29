print('-------------~~~~~~~~~~~-JSON-~~~~~~~~~~~~~~~----------------')
import json
#JSON由键值对（collecting）和对象（object）组成
#与字典的区别：1、JSON里键的数据类型必须为字符串   2、键的字符串内容必须使用双引号括起来
#函数：
# json.dumps():编码器，用来将python的对象转换成json格式的字符串
print(type(json.dumps({"c":1,"b":2,"a":3})))    #返回str
# json.loads():json格式的字符串转换为Python的对象
print(type('[1,2,3]'),type(json.loads('[1,2,3]')))    #返回字符串、列表
print(json.loads('{"vendor":"huawer","model":"USG6539"}'),type(json.loads('{"vendor":"huawer","model":"USG6539"}')))
# 返回字典
print('-------------~~~~~~~~~~~-TextFSM-~~~~~~~~~~~~~~~----------------')
#TextFSM：使用自定义的变量和规则设计模板，用模板处理文本内容，将无规律的文本内容按照模板整合成想要的有序的数据格式
import textfsm
print('-------------~~~~~~~~~~~-ntc-templates-~~~~~~~~~~~~~~~----------------')
#ntc-templates:模板集，将主流绝大数设备里输入的show/display命令得到的各式各样回显文本内容整合成json、xml、yaml
#格式
print('-------------~~~~~~~~~~~-NAPALM-~~~~~~~~~~~~~~~----------------')
#为多厂商的网络设备提供统一API的Python库，目前仅支持Cisco、Arista、Juniper设备
#NAPALM 的 API 分为 Getter 类和 Configuration 类，上面所列获取设备参数的 API 即 Getter 类，
# 而 Configuration 类则支持对设备的配置做替换(Config.replace)、合并(Config.merge)、
# 比对(Compare Config)、原子更换(Atomic Changes)、回滚(Rollback) 等操作，
# 功能比 TextFSM 和 ntc-template 更强大。
import napalm
print('-------------~~~~~~~~~~~-pyntc-~~~~~~~~~~~~~~~----------------')
import pyntc
#pyntc 是一种多厂商、多 API 的模块，让网络运维的脚本代码简捷、易懂、 便于维护。
#截至2020年5月，Pyntc支持包括 Cisco、Arista、Juniper 在内的 3 家主流设备厂商的4种操作系统。
#效果：获取目标设备的基本信息；对目标设备进行配置;获取目标设备的 running config
#对目标设备的running config进行备份;重启目标设备
print('-------------~~~~~~~~~~~-netdev异步并行-~~~~~~~~~~~~~~~----------------')
import netdev
#netdev的开源模块,该模块依赖Netmiko，并且需要至少Python3.5以上才能运行,
#最大的特点是支持对网络设备进行异步登录和操作
import asyncio
import netdev
import time
async def task(dev):
    async with netdev.create(**dev) as ios:
       commands = ["line vty 5 15", "login local","exit"]
       out = await ios.send_config_set(commands)
       print(out)
async def run():
    devices = []
    f = open('ip_list.txt')
    for ips in f.readlines():
        ip = ips.strip()
        dev = { 'username' : 'python',
                'password' : '123', 'device_type': 'cisco_ios', 'host': ip
              }
        devices.append(dev)
    tasks = [task(dev) for dev in devices]
    await asyncio.wait(tasks)
start_time = time.time()
print (f"程序于 {time.strftime('%X')} 开始执行\n")
asyncio.run(run())
print (f"\n 程序于 {time.strftime('%X')} 执行结束")
print('-------------~~~~~~~~~~-netmiko多线程-~~~~~~~~~~~~~----------------')
#多线程(Multithreading)来提 升 Python 脚本的工作效率
#coding=utf-8
from netmiko import ConnectHandler
import threading
from queue import Queue
import time
f = open('ip_list.txt')
threads = []
def ssh_session(ip, output_q):
    commands = ["line vty 5 15", "login local","exit"]
    SW = {'device_type': 'cisco_ios', 'ip': ip, 'username': 'python', 'password': '123'}
    ssh_session = ConnectHandler(**SW)
    output = ssh_session.send_config_set(commands)
    print (output)
print (f"程序于 {time.strftime('%X')} 开始执行\n")
for ips in f.readlines():
    t = threading.Thread(target=ssh_session, args=(ips.strip(), Queue()))
    t.start()
    threads.append(t)
for i in threads:
    i.join()
print (f"\n 程序于 {time.strftime('%X')} 执行结束")




