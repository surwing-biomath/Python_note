# Bug: 指的是检测并排除计算机程序/机器中的故障
# 粗心导致的语法错误的解决方案：
# 1，漏了末尾的冒号，如if语句、循环语句、else子句等
# 2，缩进错误，该缩进的没有缩进，不该缩进的乱缩进
# 3，把英文符号写成了中文符号，例如：引号、冒号、括号
# 4，字符串拼接的时候，把字符串和数字拼接在一起
# 5，没有定义变量，例如：while循环条件的变量没有定义
# 6，'=='比较运算符和'='赋值运算符的混用

# 思路不清晰导致的语法错误的解决方案：
# 1，使用print()函数
# 2，使用'#'暂时注释部分代码

# Python中异常处理机制：
# try...except的语法结构：
# try:
#     可能会抛出异常的代码
# except 异常类型:
#     异常处理代码（报错后执行的代码）

# try...except...except的语法结构：
# try:
#     可能会抛出异常的代码
# except 异常类型A:
#     异常处理代码（报错后执行的代码）
# except 异常类型B:
#     异常处理代码（报错后执行的代码）
# 捕获异常的顺序：先子类后父类的顺序，最大的异常类型（能捕获最多的异常类型；BaseException）写在最后

try:
    num1=eval(input('请输入一个整数：'))
    num2=eval(input('请输入另一个整数：'))
    result=num1/num2
    print('结果为：',result)
except ZeroDivisionError:
    print('除数为零')

try:
    num1=eval(input('请输入一个整数：'))
    num2=eval(input('请输入另一个整数：'))
    result=num1/num2
    print('结果为：',result)
except ZeroDivisionError:
    print('除数不允许为零')
except NameError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')

# try...except...else的语法结构：
# try:
#     可能会抛出异常的代码
# except 异常类型:
#     异常处理代码（报错后执行的代码）
# else:
#     没有抛异常要执行的代码

try:
    num1=eval(input('请输入一个整数：'))
    num2=eval(input('请输入另一个整数：'))
    result=num1/num2
except ZeroDivisionError:
    print('除数不允许为零')
except NameError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')
else:                                    # else 是程序正常执行结束所执行的代码
    print('结果为：',result)

# try...except...else...finally的语法结构：
# try:
#     可能会抛出异常的代码
# except 异常类型:
#     异常处理代码（报错后执行的代码）
# else:
#     没有抛异常要执行的代码
# finally:
#     无论是否产生异常都要执行的代码

try:
    num1=eval(input('请输入一个整数：'))
    num2=eval(input('请输入另一个整数：'))
    result=num1/num2
except ZeroDivisionError:
    print('除数不允许为零')
except NameError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')
else:                                    
    print('结果为：',result)
finally:
    print('程序执行结束！')