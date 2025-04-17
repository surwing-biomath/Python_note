# 常用内置函数：不需要使用前缀就可以直接使用的函数，分为数据类型转化函数、数学函数、迭代器操作函数、其他函数
# 数据类型转化函数：
# bool(obj):   获取指定对象obj的布尔值
# str(obj):    将指定对象obj转成字符串类型
# int(x):      将x转成int类型
# float(x):    将x转成float类型
# list(seq):   将序列转成列表类型
# tuple(seq):  将序列转成元组类型
# set(seq):    将序列转成集合类型

print('非空字符串的布尔值：',bool('hello'))  # True
print('空字符串的布尔值：',bool(''))         # False   # 空字符串不是空格字符串
print('空列表的布尔值：',bool([]))           # False
print('空列表的布尔值：',bool(list()))       # False
print('空元组的布尔值：',bool(()))           # False
print('空元组的布尔值：',bool(tuple()))      # False
print('空集合的布尔值：',bool(set()))        # False
print('空字典的布尔值：',bool({}))           # False
print('空字典的布尔值：',bool(dict()))       # False
print('-'*50)
print('非0数值型的布尔值：',bool(123))       # True
print('整数0的布尔值：',bool(0))             # False
print('浮点数0.0的布尔值：',bool(0.0))       # False
print('-'*50)

# 将其他类型转成字符串类型
lst=[10,20,30]
print(type(lst),lst)                       # <class 'list'> [10, 20, 30]

s=str(lst)
print(type(s),s)                           # <class 'str'> [10, 20, 30]
print('-'*50)

# float类型和str类型转成int类型
print(int(98.7)+int('90'))                 # 188
# 注意事项
# print(int('98.7'))                       # ValueError: invalid literal for int() with base 10: '98.7'
# print(int('a'))                          # ValueError: invalid literal for int() with base 10: 'a'
print('-'*50)

# int类型和str类型转成float类型
print(float(90)+float('3.14'))             # 93.14
print('-'*50)

s='hello'
print(list(s))                             # ['h', 'e', 'l', 'l', 'o']

seq=range(1,11)
print(list(seq))                           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(seq))                          # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(set(seq))                            # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 数学函数：
# abs(x):                                  # 绝对值
# divmod(x,y):                             # 获取x除以y的商和余数
# max(seq):                                # 获取序列seq最大值
# min(seq):                                # 获取序列seq最小值
# sum(iter)                                # 对可迭代对象iter进行求和运算
# pow(x,y)                                 # x的y次幂
# round(x,d)                               # 对x保留d位小数，结果四舍五入

print('绝对值：',abs(100),abs(-100),abs(0)) # 100 100 0
print('商和余数：',divmod(13,4))            # (3, 1)
print('最大值：',max('hello'))              # o          # 按照ASCII码值进行计算
print('最大值：',max([10,4,56,78,4]))       # 78
print('最小值：',max('hello'))              # e          # 按照ASCII码值进行计算
print('最小值：',max([10,4,56,78,4]))       # 4
print('求和：',sum([10,34,45]))             # 89
print('幂次',pow(2,3))                      # 8

# 四舍五入 
print(round(3.1415926))                     # 3          # round函数只有一个参数时，四舍五入保留整数
print(round(3.9415926))                     # 4          
print(round(3.1415926,2))                   # 3.14
print(round(314.15926,-1))                  # 310.0      # -1位，对个位进行四舍五入
print(round(394.15926,-2))                  # 400.0      # -2位，对十位进行四舍五入
print('-'*50)

# 迭代器操作函数，操作可迭代对象，例如字符串、列表、元组，都可以使用for循环进行遍历操作
# sort(iter):                               # 对可迭代对象进行排序
# reversed(seq):                            # 反转序列生成新的迭代器对象
# zip(iter1,iter2):                         # 将iter1与iter2打包成元组并返回一个可迭代的zip对象
# enumerate(iter):                          # 根据iter对象创建一个enumerate对象
# all(iter):                                # 判断可迭代对象iter中所有元素的布尔值是否都为True
# any(iter):                                # 判断可迭代对象iter中所有元素的布尔值是否都为False
# next(iter):                               # 获取迭代器的下一个元素
# filter(function,iter):                    # 通过指定条件过滤序列并返回一个迭代器对象
# map(function,iter):                       # 通过函数function对可迭代对象iter的操作返回一个迭代器对象

lst=[54,56,77,4,567,34]
# (1)排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表：',lst)                        # [54, 56, 77, 4, 567, 34]
print('升序：',asc_lst)                      # [4, 34, 54, 56, 77, 567]
print('降序：',desc_lst)                     # [567, 77, 56, 54, 34, 4]
print('-'*50)

# (2)reverse反向
new_lst=reversed(lst)
print(type(new_lst))                        # <class 'list_reverseiterator'> # 迭代器对象
print(list(new_lst))                        # [34, 567, 4, 77, 56, 54]
print('-'*50)

# (3)zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))                         # <class 'zip'>
print(list(zipobj))                         # [('a', 10), ('b', 20), ('c', 30), ('d', 40)]
print('-'*50) 

# (4)enumeerate
enum=enumerate(y,start=1)
print(type(enum))                           # <class 'enumerate'>
print(tuple(enum))                          # ((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))
print(list(enum))                           # []
print('-'*50)

# (5)all any
lst2=[10,20,'',30]
print(all(lst))                             # True
print(all(lst2))                            # False

print(any(lst))                             # True
print(any(lst2))                            # True

# next
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))
print(next(zipobj))                         # ('a', 10)
print(next(zipobj))                         # ('b', 20)
print(next(zipobj))                         # ('c', 30)
print('-'*50)

obj=filter(lambda num:num%2==1,range(10))
print(type(obj))                            # <class 'filter'>
print(list(obj))                            # [1, 3, 5, 7, 9]

new_lst2=['hello','world','python']
obj2=map(lambda x:x.upper(),new_lst2)
print(type(obj2))                           # <class 'map'>
print(list(obj2))                           # ['HELLO', 'WORLD', 'PYTHON']
print('-'*50)


# 其他内置函数：
# format(value,format_spec):                # 将value以format_spec格式进行显示
# len(s):                                   # 获取s的长度或s元素的个数
# id(obj):                                  # 获取对象的内存地址
# type(x):                                  # 获取x的数据类型
# eval(s):                                  # 执行s这个字符串所表示的Python代码

# format()
print(format(3.14,'20'))                    #                 3.14          # 数值型默认右对齐
print(format('hello','20'))                 # hello                         # 字符串默认左对齐
print(format('hello','*<20'))               # hello***************          # <左对齐，*表示填充符，20表示的是显示的宽度
print(format('hello','*>20'))               # ***************hello
print(format('hello','*^20'))               # *******hello********
print('-'*50)

print(format(3.1415926,'.2f'))              # 3.14
print(format(20,'b'))                       # 10100
print(format(20,'o'))                       # 24
print(format(20,'x'))                       # 14
print(format(20,'X'))                       # 14
print('-'*50)

print(len('helloworld'))                    # 10
print(len([10,20,30,40,50]))                # 5
print('-'*50)

print(id(10))                               # 140732596290760
print(id('helloworld'))                     # 3021896764144
print(type('hello'),type(10))               # <class 'str'> <class 'int'>
print('-'*50)

print(eval('10+30'))                        # 40
print(eval('7/6'))                          # 1.1666666666666667
print(eval('10>30'))                        # False

def fun(n):
    lst=[2,8]
    for i in range(1,n):
        lst.append(lst[-1]+lst[-2])
        return lst[-2]%lst[-1]              # return执行一次就结束函数
print(fun(7))                               # 8            

def fun1():
    print('helloworld')
print(type(fun1),type(fun1()))              # <class 'function'> <class 'NoneType'>

