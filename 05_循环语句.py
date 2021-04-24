#coding=utf-8
print('---------------------------------While循环----------------------------------------------')
#while循环：根据判断语句返回值决定是否再次执行该程序；True继续，False终止，break强行终止，格式：while 判断语句：
print('''请根据对应的号码选择一个设备型号：
1. USG6320
2. USG6395
3. USG9500
4. SW5700
5. CE12800
6. AntiDDOS8000
''')
while True:       #手动指定true，判定条件永久成立
    Model_option=input('请输入您的选项（数字1-6）：')
    if Model_option.isdigit() and int(Model_option) in list(range(1,7)):
        if int(Model_option) in list(range(1,4)):
            print('该设备为华为下一代USG防火墙。')
        elif int(Model_option) in list(range(4,6)):
            print('该设备为华为三层交换机或云引擎交换机')
        else:
            print('该设备为华为防护DDos攻击安全设备')
        break       #当输入正确则终止整个while循环， 否则重复执行input语句直到输入正确为止
    else:
        print('您的输入无效，请重新输入')
print('---------------------------------for循环----------------------------------------------')
#for循环：遍历一组可迭代的序列（字符串、列表、元组等），遍历完循环即终止，格式：for item in sequence： statement
LinkState_protocals=['ospf','isis']
for protocal in ('bgp','isis','igrp','eigrp','ospf','rip'):      #元组作为可迭代的序列
    if protocal not in LinkState_protocals:
        print(protocal,'不属于链路状态路由协议')



