print('----------------------------------Open函数及其模式----------------------------------------------')
#open（）:打开一个文本文件并创建一个文件对象
#r模式：以只读方式打开文件，只能打开已存在的文件
#w模式：打开文件并只用于写入；文件存在，则原有内容删除覆盖；文件不存在，则创建新文件
#a模式：追加方式打开文件；文件存在，新内容添加原有内容之后；文件不存在，则创建新文件
#r+：以读写方式打开文件，只能打开已存在的文件
#w+：以读写方式打开文件；文件存在，则原有内容删除覆盖；文件不存在，则创建新文件
#a+：以读写方式打开文件；文件存在，新内容添加原有内容之后；文件不存在，则创建新文件
#read()、readline()、readlines()不支持a模式（追加）、w模式（写入）
print('----------------------------------read()方法用法----------------------------------------------')
#read（）方法读取文件内全部内容，返回值为字符串;seek（）修改文件指针在文件中位置；tell（）显示当前文件指针的位置
Device_Vendors=open('/Volumes/存储/python/Note/files/Vendors.txt')
print('文件指针当前位置：',Device_Vendors.tell())
print(Device_Vendors.read().strip())             #strip()函数移除字符串开头/结尾字母、数字、空格、换行、标点符号
print('文件指针当前位置：',Device_Vendors.tell())   #文件指针从文件开头移动到末尾,打印为空
print('打印为空',Device_Vendors.read())
Device_Vendors.seek(0)                                #将文件指针从末尾移至开头
print('文件指针当前位置：',Device_Vendors.tell())        #打印文件指针的当前位置0
print(Device_Vendors.read())
print('--------------------------------readline()方法用法--------------------------------------------')
#readline()方法：一排一排的读取文件的内容，返回值是字符串，每次返回文件的一排内容
Device_Vendors=open('/Volumes/存储/python/Note/files/Vendors.txt')
print(Device_Vendors.readline().strip())
print(Device_Vendors.readline().strip())
print(Device_Vendors.readline().strip())
print(Device_Vendors.readline().strip())
print(Device_Vendors.readline().strip())     #strip()去掉末尾换行符
print(Device_Vendors.readline().strip())     #由于文件指针移动到末尾，打印为空
print('-------------------------------readlines()方法用法-------------------------------------------')
#readlines()方法：返回值为带\n的列表；一排一排的读取文件内容，每排的内容以列表元素的形式返回
ip_address=open('/Volumes/存储/python/Note/files/Ip_list.txt')
print(len(ip_address.readlines()))       ##readlines读取返回列表，再用len（）函数判断该列表的长度，即文件中IP地址数量
ip_address.seek(0)                      #修改文件指针的起始位
for ip in ip_address.readlines():
    if ip.startswith('172.16.'):        #条件判断，采用startswith方法找出'172.16.'起始的字符串
        print(ip.strip())               #strip()方法去掉换行符\n，保证美观





