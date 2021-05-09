print('----------------------------------write函数及其模式----------------------------------------------')
#r+:新内容添加在文件的开头，并覆盖原来已有的内容
f = open('/Volumes/存储/python/Note/files/07_test.txt','r+')    #读写打开文件，只能打开已存在文件
print(f.write('Juniper\n'))     #f.write类型为int
f.close()                       #close方法关闭，文件才可保存
#w/w+:新内容添加在文件开头，已存在的内容会被完全清空
f = open('/Volumes/存储/python/Note/files/07_test.txt','w')
f.write('test')
f.close()
f = open('/Volumes/存储/python/Note/files/07_test.txt','w+')
f.write('''Cisco
Juniper
Huawei
H3C
Watchguard
''')
f = open('/Volumes/存储/python/Note/files/07_test.txt')
Vendor = f.readlines()
print(Vendor)
f.close()
#a/a+:新内容添加在文件末尾，已存在的内容不会被清空
f = open('/Volumes/存储/python/Note/files/07_test.txt','a')
f.write('CheckPoint\n')
f = open('/Volumes/存储/python/Note/files/07_test.txt','a+')
f.write('Aruba')
f.close()             #保存
f = open('/Volumes/存储/python/Note/files/07_test.txt')
Vendor = f.readlines()
print(Vendor)
#closed方法：判断文件是打开还是关闭，返回布尔型False/True
f = open('/Volumes/存储/python/Note/files/07_test.txt')
print(f.closed)           #False
f.close()
print(f.closed)           #True
#with语句：管理文件对象，用with语句打开的文件将被自动关闭   with ... as 变量:
with open('/Volumes/存储/python/Note/files/07_test.txt') as f:
     print(f.read())        #read方法读取文件内全部内容，返回值为字符串,而readlines方法返回值为带\n的列表
print(f.closed)             #with自动关闭文件，返回True





