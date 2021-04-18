#!/usr/bin/env python3  ##采用python3解释器
#coding=utf-8   ##编码支持中文修改方法一
#code=utf8   ##编码支持中文修改方法二
#--------------------------demo1----------------------------------------------
age=input('请输入您的年龄？')
print('your age is:'+ str(age))    #str()方法将用户输出的int转换为str，才能+拼接
#--------------------------demo2----------------------------------------------
#假设IP地址的第3段为用户所在楼层，用户输入IP地址，py自动告知所在楼层
ip = input("请输入您的IP地址:")
ip_list=ip.split('.')             #split方法用做将字符串转换为列表、split('.')中的.为分隔符，用做对字符串进行切片，因为IP地址采用点分十进制，所以这里采用点。
print('您所在的楼层为：'+ip_list[2]+'楼')     #字符串+列表索引+字符串的拼接
#--------------------------demo3----------------------------------------------
commands=['system view','interface Gi0/0/0','ip addrese = 10.1.1.21 24']    ##创建华为USG设备配置管理口IP地址的命令的列表
commands_enter='\n'.join(commands)         ##利用join方法将\n换行符加在每条命令的末尾，不然防火墙执行命令报错！！！
print(commands_enter)
#--------------------------demo4----------------------------------------------
ip_add='.'.join(['192','168','100','200']) ##将IP地址组成的列表还原成字符串192.168.100.200，需采用join方法在列表元素末尾加上点号.       
print(ip_add)
#--------------------------demo5----------------------------------------------
##startswith：用来判断字符串是否以给定的字符串开头
##endswith：用来判断字符串是否以给定的字符串结尾
ip_1='192.168.100.250'
print(ip_1.startswith('192.1'))     #true
print(ip_1.startswith('182'))       #false
ip_2='192.168.200.250'             
print(ip_2.endswith('50'))          #true
print(ip_2.endswith('.260'))        #false
#--------------------------demo6----------------------------------------------
##isdigit方法：判断字符串内容是否为整数
##isalpha方法：用来判断字符串的内容是否为英文字母，哪怕出现空格、下划线等特殊字母，也会返回False
date='20210417'
print(ip_1.isdigit())        #false
print(date.isdigit())        #true
Device='Huawei'
Domain='huawei.com'
print(Device.isalpha())      #true
print(date.isalpha())        #false
print(Domain.isalpha())      #false
#--------------------------demo7----------------------------------------------
#int：不带小数点的正数或负数    float：带小数点的正数或负数
#可通过type（）查看  
type(25) 
type(3.1415926)
#--------------------------demo8----------------------------------------------
#算术运算符
#+、-、*乘、/除法求商、//向下取整求商数、%求余数、**幂运算，如：3的3次方位3**3
print('HCIE '*8)          #输出8次HCIE，注意后有空格
print('HCIE '+'HCIE')     #第一个HCIE后有空格
print('*'*50)             #打印50次星号
#计数器用法
counter=0
counter=counter+1   #写法一 
print(counter)      #1
counter+=1          #写法二
print(counter)      #2
counter+=1
print(counter)      #3
counter+=1
print(counter)      #4







