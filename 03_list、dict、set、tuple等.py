#!/usr/bin/env python3
#coding=utf-8
#------------------------------------【列表用法】----------------------------------------------
print('--------------【列表用法】-----------------')
#列表是一种有序集合,[]表示，其中的数据被称为元素（element），彼此用逗号隔开，元素的数据类型可以不固定，可用type()方法验证数据类型
hcie_list=[2021,3.142159,'huawei',False,None,['Writing',2,'interview']]    #int、float、str、boolean、空、list
print(hcie_list[5][2])                                                     #两次索引调取列表中列表的元素
#python2中range（）函数用来创建整数列表如：a=range(1,30,3)列表：起始位1 结束位30 步长3
#为了节省内存，python3中range（）函数返回值为range，可以被迭代的对象
a=list(range(10))                                                          #默认0开始，10-1结束
b=list(range(1,50,2))                                                      #采用list函数使range（）返回列表
print(a)
print(b)
#append（）用来向列表最后面添加新元素
interfaces=[]
interfaces.append('Gi0/0/0')
print(interfaces)
interfaces.append('Gi1/0/0')                  #！！！注意append()只接受一个参数传递
print(interfaces)
#len（）用来统计列表中有多少个元素
print(len(interfaces))                        #2
#count（）用来找出指定元素在列表中的个数，返回值为整数
device_modes=['cisco','juniper','huawei','h3c','huawei','CheckPoint''Huawei','Fortinet','HPE','huawei']
print(device_modes.count('huawei'))           #3 ,区分大小写
#insert（）向列表插入元素，但可以自由定义新元素在列表中的位置
ospf_configuration=['ospf 1','default-route-advertise always','network 10.1.10.0 0.0.0.255']
ospf_configuration.insert(0,'system view')       #起始位0插入新元素
ospf_configuration.insert(3,'area 0.0.0.0')      #起始位3插入新元素
print(('\n'.join(ospf_configuration)))           #采用join（）方法在列表每个元素末尾插入换行符\n
#pop（）用来移除列表中的元素。不指定索引号，默认移除列表末尾的元素；如指定索引号，可精确移除特定位置的元素
huawei_device_models=['2110','2220','3200','USG6220','USG6320','USG6239','USG9000','WAF-5000','FireHunter6000','AntiDDOS-8000','ATIC']
huawei_device_models.pop()                       #默认去掉末尾元素，’ATIC‘
huawei_device_models.pop(5)                      #索引5，去掉’USG6239‘
print(huawei_device_models)
#index（）用来确认元素在列表中的索引号
huawei_device_models=['2110','2220','3200','USG6220','USG6320','USG6239','Ruijie','USG9000','WAF-5000','FireHunter6000','AntiDDOS-8000','ATIC']
index=huawei_device_models.index('Ruijie')       #找出元素’Ruijie‘在列表中的索引：6
print(index)                                     #6
#------------------------------------【字典用法】----------------------------------------------
print('--------------【字典用法】-----------------')
#字典是若干组无序的键值对（key-value-pair）的集合，用大括号{}表示，每一组键值对用逗号隔开；键值对用冒号：隔开
dict={'Vendor':'Huawei','Model':'USG6320','Ports':8,'VRP':'V500R005C00SPC100','CPU':3.8}       #键可为str、int、float、元组；值可为任意的类型
print(dict)                             
print(dict['VRP'])                      #查找字典里某个键对应的值，格式：字典名['键名']                             
dict['StartTime']=[202104181100]        #字典里新添加一组键值对，格式：字典名[新键名]=新值
print(dict)
dict['Ports']=10                        #更改字典里某个已有键对应的值，格式：字典名[键名]=新值
print(dict)
del dict['StartTime']                   #删除字典里某组键值对，格式：del 字典名[键名]
print(dict)                             #去掉开机时间的键值对
#len（）用来统计字典里有多少组键值对，len（）的返回值是整数
print(len(dict))                        #5
#keys（）用来返回字典里所有的键，python3中返回值为迭代的对象，需要使用list（）转换为列表
print(dict.keys())                      #返回所有键，为可迭代的对象
print(list(dict.keys()))                #返回所有键，采用list方法转换为列表
for key in dict:                        #采用for in遍历字典里的所有key，并自动换行
    print(key)                          #注意缩进
#values（）用来返回字典里所有的值，python3中返回值为迭代的对象，需要使用list（）转换为列表
print(dict.values())                    #返回所有值，为可迭代的对象
print(list(dict.values()))              #返回所有值，采用list方法转换为列表
for values in dict.values():            #采用for in遍历字典里的所有values，并自动换行；与遍历key方法不同，注意！！！
	print(values)                       #注意缩进
#pop（）用来删除字典中的键值对；导入键名，返回值是键对应的值
dict={'Vendor':'Huawei','Model':'USG6320','Ports':8,'VRP':'V500R005C00SPC100','CPU':3.8,'Memory':'8GB'}
print(dict.pop('Memory'),'\n',dict)     #pop（键名）返回为值8GB、\n换行、打印删除后的dict
#get（）返回字典里具体键名对应的值，返回结果为导入键名所对应的值
print(dict.get('Vendor'),dict.get('CPU'),dict.get('Memory'))   #返回Vendor和CPU对应的值，应为Memory前文已用pop（）删除，故此处返回none 
#------------------------------------【布尔类型】----------------------------------------------  
print('--------------【布尔类型】-----------------')   
#True和False，首字母必须大写
#比较运算符：==（等于）、！=（不等于）、>（大于）、<（小于）、>=（大于等于）、<=（小于等于），返回值是布尔值
a=100
print(a==100)          #True
print(a>=120)          #Falue 
#逻辑运算符：and（与）、or（或）、not（非）
A=False
B=False
print(A and B)         #False
print(A or B)          #False
print(not A)           #True
#------------------------------------【集合、元组、空值】----------------------------------------------  
print('---------------【集合、元组、空值】-----------------')   
#集合（set）：一种没有重复元素的特殊列表，可以通过{}或者set（）函数创建；集合是无序的，不能适用索引号、index（）函数、count（）方法
interfaces={'Gigabitethernet1/0/1','Gigabitethernet1/0/2','Gigabitethernet1/0/3','Gigabitethernet1/0/4'}    #{}创建集合
print(type(interfaces),interfaces)                                                                          #输出集合类型、集合元素
Vendors=set(['cisco','Huawei','Ruijie','juniper','Fortinet','Huawei'])                                      #set()函数创建集合
print(type(Vendors),Vendors)                                                                           #输出集合类型、集合元素，自动去掉重复的元素’Huawei‘
#add（）：用来向一组集合添加新元素，返回值依然是集合
print(Vendors.add('CheckPoint'),'\n',Vendors)                   #Vendors.add('CheckPoint')返回空、换行、新增元素后的集合
#remove（）：用来删除一组集合中已有的元素，返回值依然是集合
print(Vendors.remove('CheckPoint'),'\n',Vendors)                #Vendors.remove('CheckPoint')返回空、换行、删除元素后的集合
#元组（Tuple）
#1.是一种特殊的列表，列表可以任意对元素增、删、改，而元组一旦创建，无法做任何形式的更改；元组只保留index（）、count（）两种方法
#2.元组可以小括号（）创建，也可以tuple（）函数创建，元组是有序的，支持索引
Vendors=('Huawei','Ruijie','Cisco','Aliyun')         #小括号（）创建元组
print(type(Vendors),Vendors,Vendors[3])              #返回变量类型tuple、元组元素、元组中索引3的元素   
Vendors2=['Huawei0','Ruijie1','Cisco2','Aliyun3','Huawei0']
print(type(tuple(Vendors2)),tuple(Vendors2),tuple(Vendors2)[3])        #使用tuple（）函数将类别转换为元组
#index（）：用来查询指定元素的索引号，返回值为整数
print(Vendors.index('Huawei'))       #0
#conut（）：用来查询指定元素在元组中的个数，返回值为整数
print(Vendors2.count('Huawei0'),Vendors2.count('juniper'))     #2,0
#空值（None）
#1.特殊的数据类型，没有自带的函数和方法，无法做任何算术和逻辑运算
#2.但是可以被赋值给一个变量
#3.常用在判断语句、正则表达式中，用于抓取网络设备中需要查询或排错的命令信息，判断是否抓取成功。
a=None
print(type(None),None==100,a)        #输出空None类型、逻辑运算False、a的赋值None











