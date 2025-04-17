# Python中的异常处理：
# raise关键字：抛出一个异常，从而提醒程序出现了异常情况，程序能够正确地处理这些异常情况
# raise关键字语法架构：raise [Exception类型(异常描述信息)]

# try:
#     gender=input('请输入您的性别：')
#     if gender!='男' and gender!='女':
#         raise Exception('性别只能是男或女')
#     else:
#         print('您的性别是：',gender)
# except Exception as e:
#     print(e)

# Python中常见的异常类型：
# ZeroDivisionError:    除数为零
# IndexError:           索引超出范围
# KeyError:             字典取值时key不存在
# NameError:            使用一个没有声明的变量
# SyntaxError:          Python中的语法错误
# ValueError:           传入的值错误
# AttributeError:       属性或方法不存在
# TypeError:            类型不合适
# IndentationError:     不正确的缩进

# (1) ZeroDivisionError
# print(10/0)

# (2) IndexError
# lst=[10,20,30,40]
# print(lst[4])

# (3) KeyError
# dict={'name':'louis','age':20}
# print(dict['gender'])

# (4) NameError
# print(hello)

# (5) SyntaxError
# print('hello)

# (6) ValueError
# print(int('a'))

# (7) AttributeError
# i=10
# print(i.name)

# (8) TypeError
# print('hello'+123)

# (9) IndentationError
    # print('hello')

# 使用PyCharm进行代码调试的操作步骤：
# 1，设置断点，通常设置在函数定义处、循环处
# 2，进入调试试图
# 3，开始调试
