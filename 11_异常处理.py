#语法错误（Syntax Errors）和异常（Exceptions）
#零除错误
#print(100/0)                      #错误类型：ZeroDivisionError: division by zero
#命名错误
#print(name)                       #错误类型：NameError: name 'name' is not defined
#类型错误
a = 10
#print('there are'+ a +'books.')   #错误类型：TypeError: can only concatenate str (not "int") to str
#I/O错误
#f = open('abc.txt')               #错误类型：FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
#paramiko模块：ssh用户密码错误相关的AuthenticationException、ip地址不可达相关socket模块的socket.error
#try...except...语句做异常处理
for i in range(2,8):
    try:
        if i == 2:
          print(i/0)               #有异常，程序不会终止，继续执行else后语句，打印3，4，5，6，7
        else:
          print(int(i/1))
    except ZeroDivisionError:
        print('Division by 0 is not allowed')
#不知道异常类型，可使用except：和Exceptions捕获所有异常
try:
    100/0
except:                   #不接任何异常类型
    print("There's an error.")

try:
    a=10
    print('there are'+ a +'apples')
except Exception as e:    #用Exceptions捕获除SystemExit、KeyboardInterrupt、GeneratorExit外所有异常
    print(e)              #打印出来

try:
    a=10
    print('there are'+ a +'apples')
except BaseException as f:
    print(f)              #用BaseExceptions捕获SystemExit、KeyboardInterrupt、GeneratorExit三种异常




