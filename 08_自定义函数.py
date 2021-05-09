print('----------------------------------自定义函数----------------------------------------------')
#r+:新内容添加在文件的开头，并覆盖原来已有的内容
#函数：组织好的可以被重复使用的一组代码块，用来提高代码的重复使用率，分为内建函数（Built-in Function）和自定义函数
#def语句创建自定义函数，def 函数名() 括号内可带参数和不带参数，要调用该函数，才能得到函数的输出结果
def count(x,y):
    result = x*y
    print(result)
(count(5,5))     #3->赋值给x，5->赋值给y  调用count函数做*运算
#函数必须先定义创建，才可被调用！
#函数的返回值：print、return语句，函数没有使用print/return,则函数返回空值none
#区别：print语句不保留返回结果，直接打印控制台，而return返回值不会打印输出控制端，且可以赋值给另一个变量
def Model():
    print('Huawei')
Model()              #一次打印Huawei
a = Model()          #再次调用函数，二次打印Huawei
print(a)             #函数内print语句不保存返回值，打印none
def Exam():
    return 'HCIE'
Exam()               #不打印return返回值
print(Exam())        #print语句打印return返回值，打印HCIE
a = Exam()           #将ruturn返回值赋值给变量a
print(a)             #打印HCIE
print('-----------------------------------嵌套函数-----------------------------------------------')
#函数可以嵌套，即一个函数可以在另一个函数中被调用
def square(x,y):
    result = x ** y              #求x的y次方，赋值给result
    return result
def cube(z):
    result = square(3,4)*z       #3赋值给x，4赋值给y，得到3的4次方为81，然后*5得到405
    return result
cube(5)                          #5赋值给z
print(cube(5))                   #打印输出结果405






