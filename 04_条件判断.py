#coding=utf-8
print('--------------------------demo1----------------------------------------------')
#条件判断：通过比较运算符（==、!=、>、>=、<、<=）
hcie_score=input('请输入您的HCIE笔试分数：')
if int(hcie_score)>600:
    print('恭喜您通过考试，请准备实验考试！')
elif int(hcie_score)==600:
    print('恭喜您压线通过考试，请准备实验考试！')
else:
    print('成绩不及格！')
print('--------------------------demo2----------------------------------------------')
#字符串方法：isdigit()判断是否为整数、isalpha()判断是否为英文字母
#通过字符串方法+逻辑运算符（and、or、not）做判断
print('''请输入对应的号码来选择一个路由协议:
1. RIP
2. IGRP
3. EIGRP
4. OSPF
5. ISIS
6. BGP ''')
Route_option=input('请输入您的选项（数字1-6）：')
if Route_option.isdigit() and 1<=int(Route_option)<=6:
    if int(Route_option)==1 or int(Route_option) ==2 or int(Route_option)==3:    #int函数转换为整型，才可做比较运算￥
       print('该路由协议为距离矢量路由协议')
    elif Route_option=='4' or Route_option=='5':
       print('该路由协议为链路状态路由协议')
    else:
       print('该路由协议为路径矢量路由协议')
else:
    print('输入无效，请重新输入！')
print('--------------------------demo3----------------------------------------------')
#成员运算符（in、not in）配合range函数+list函数返回的整数列表，判断用户输入的选项号码是否存在于列表中
#由此对上述代码做优化
print('''请输入对应的号码来选择一个路由协议:
1. RIP
2. IGRP
3. EIGRP
4. OSPF
5. ISIS
6. BGP ''')
Route_option=input('请输入您的选项（数字1-6）：')
if Route_option.isdigit() and int(Route_option)  in list(range(1,7)):
    if int(Route_option) in list(range(1,4)):
        print('该路由协议为距离矢量路由协议')
    elif int(Route_option) in list(range(4,6)):
        print('该路由协议为链路状态路由协议')
    else:
        print('该路由协议为路径矢量路由协议')
else:
    print('输入无效，请重新输入！')


