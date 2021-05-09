#正则表达式：regex、regexp、re，用做精确匹配和模糊匹配；验证正则表达式的在线模拟器regex101
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~精确匹配~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#精确匹配：明文给出想要匹配的模式
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~模糊匹配~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#模糊匹配：匹配符号、特殊序列
#匹配符号:
# .匹配除换行符外所有字符1次
# *匹配左边字符0次或多次
# +匹配左边字符1次或多次
# ?匹配左边字符0次或1次
# {m}匹配左边字符m次
# {m,n}匹配左边字符最小m，最大n次
# {m,}匹配左边字符最小m，最多无限次
# {,n}匹配左边字符最小0，最多n次
# \  转义字符，用来匹配上述的'匹配符号'，也可表示特殊序列
# [] 匹配字符集合，如数字[0-9]、小写字母[a-z]、大写字母[A-Z]、数字字母下划线[0-9a-zA-Z_];^表示取非,非数字字符[^0-9]
# | 表示或匹配，匹配其中任意一项即可
# () 组合，匹配括号内的任意正则表达式，并表示组合的开始和结尾，如：(b|cd)ef表示匹配bef或cdef
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~贪婪匹配~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#尽可能多的匹配符号条件的内容
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~非贪婪匹配~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#在上述6种贪婪匹配符号后面加上问号？即可实现：*？  +？ ？？ {m,n}?
#在匹配到第一个字符后，随即停止
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~特殊序列~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#特殊序列由转义\和一个字符组成
# \d  匹配任意一个十进制数字，等同于[0-9]
# \D  \d取非，匹配任意一个非十进制数字，等同于[^0-9]
# \w  匹配任意一个字母、十进制数字及下划线，等同于[a-zA-Z0-9_]
# \W  \w取非，等价于[^a-zA-Z0-9_]
# \s  匹配任意一个空白字符，包括空格、换行符\n
# \S  \s取非，匹配任意一个非空白字符
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python中应用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
import re            #导入正则表达式内建模块
print(dir(re))       #查看re中的内建函数和方法
#re.match：字符串的起始位置匹配指定模式，如匹配成功，则返回值为匹配到的对象；查看匹配到对象的具体值，则需要调用group()函数
#re.match(pattern,string,flags=0)   正则模式、匹配的字符串、flags为可选项，控制正则的匹配方式
re_match_test = 'Test match（） function of regular expression.'
a = re.match(r'Test',re_match_test)      #r代表避免产生歧义的原始字符串，在re_match_test变量中匹配字符串test
print(a)                                 #返回一个匹配到的对象
print(a.group())                         #利用group方法查看匹配对象的具体值,数据类型为字符串
print(re.match(r'of',re_match_test))     #由于of不在字符串起始位置，故返回None
#re.search：在字符串的任意位置匹配指定的模式，返回值为字符串
#re.search(pattern,string,flags=0) ，和match一样一次只能匹配一个字符串内容
re_search_test = 'Test search（） function of regular expression.'
b = re.search(r'function',re_search_test)
print(b,b.group())                       #返回匹配的对象、具体值
f = open('/Volumes/存储/python/Note/files/Ip_list.txt')
for line in f.readlines():
    ipaddr = line.strip()                #strip()去除换行
    print(ipaddr)
ipaddr = '''
172.16.1.2
172.16.1.200
172.16.1.210
hcie ccie jncie
172.16.80.33
172.16.90.200
10.1.1.200
         '''
re_search_ipaddr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ipaddr)
print(re_search_ipaddr.group())
re_search_ipadd = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',ipaddr)
print(re_search_ipadd.group())
#re.findall:可以返回多个被模式匹配到的字符串，返回值为列表，每个匹配到的字符串为列表中的元素
#re.findall(pattern,string,flags=0)
re_findall_ipaddr = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ipaddr)
print(type(re_findall_ipaddr),re_findall_ipaddr)      #返回list类型、所有IP地址
#re.sub():替换字符串里被匹配到的字符串内容，返回值为字符串
#re.sub(pattern,replacement,string,optional flags) 正则模式，替换后的字符串内容，flags指定替换字符串内容的数量（空缺则默认全部替换）
usg_sessions = '''
Current Total Sessions : 3
 ftp  VPN: public --> public  ID: c487fd4e7dc57d012bf602297cd
 Zone: trust --> untrust  TTL: 00:20:00  Left: 00:19:59
 Interface: GigabitEthernet1/0/1  NextHop: 1.1.1.1  MAC: 00e0-fc82-50b8
 <--packets: 14 bytes: 931 --> packets: 15 bytes: 736
 10.1.1.100:2057[1.1.1.23:2051] +-> 2.2.2.200:21 PolicyName: trust_untrust_ftp
 
 ftp-data  VPN: public --> public  ID: c487fd4e7dc59b04523602297d2
 Zone: untrust --> trust  TTL: 00:04:00  Left: 00:03:58
 Interface: GigabitEthernet1/0/0  NextHop: 10.1.1.100  MAC: 5489-983a-65a4
 <--packets: 1 bytes: 44 --> packets: 2 bytes: 84
 2.2.2.200:20 --> 1.1.1.23:2053[10.1.1.100:2059] PolicyName: trust_untrust_ftp
 
 ftp-data  VPN: public --> public  ID: c487fd4e7dc58c0fe68602297cd
 Zone: untrust --> trust  TTL: 00:00:10  Left: 00:00:05
 Interface: GigabitEthernet1/0/0  NextHop: 10.1.1.100  MAC: 5489-983a-65a3
 <--packets: 3 bytes: 124 --> packets: 5 bytes: 561
 2.2.2.200:20 --> 1.1.1.23:2052[10.1.1.100:2058] PolicyName: trust_untrust_ftp
 '''
re_sub_sessions = re.sub(r'\w{4}\-\w{4}\-\w{4}','1234-56ab-cdef',usg_sessions)
#usg_sessions中所有mac替换为1234-56ab-cdef
print(re_sub_sessions)
print(re.sub(r'\w{4}\-\w{4}\-\w{4}','1234-56ab-cdef',usg_sessions,1))
#optional flags置1，仅替换第一条会话中的mac地址为1234-56ab-cdef
print(re.sub(r'\w{4}\-\w{4}\-\w{3}[3]','1234-56ab-cdef',usg_sessions))
#[3]精确匹配0-9中的3，即替换mac地址最后一位为3的mac为1234-56ab-cdef，即第三条session

