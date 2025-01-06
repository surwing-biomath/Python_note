# 函数：将一段实现功能的完整代码，使用函数名称进行封装，通过函数名称进行调用。以此达到一次编写，多次调用的目的
# 1，内置函数：输入函数input(),输出函数print(),列表定义函数list()
# 2，自定义函数：
# def 函数名称（参数列表）：
#     函数体
#     [return返回值列表]  # return非必须，函数可以没有返回值
# 3，函数调用：函数名（参数列表）

def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为：{s}')

# get_sum()函数的调用
get_sum(10)
get_sum(100)
get_sum(1000)

# 函数定义处的参数是形式参数（num），函数调用处传入的参数是实际参数（10,100,1000）

# 函数的参数传递：
# 位置参数：指调用时的参数个数和顺序必须与定义的参数个数和顺序相同
# 关键字参数：在调用函数时，使用“形式参数名称=值”的方式进行参数的传递，传递参数的顺序可以与定义时参数的顺序不同
# 默认值参数：在函数定义时，直接对形式参数进行赋值，在调用时如果该参数不传值，将使用默认值，如果该参数传值，则使用传递的值

# 位置参数的使用
def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 函数调用
# happy_birthday('louis')        # TypeError: happy_birthday() missing 1 required positional argument: 'age'

# happy_birthday(18,'louis')     # TypeError: can only concatenate str (not "int") to str

happy_birthday('louis',18)


# 关键字参数的使用
happy_birthday(age=18,name='louis')     # 调用处关键字参数必须与定义处的形式参数完全一致
# happy_birthday(age=18,name1='louis')  # TypeError: happy_birthday() got an unexpected keyword argument 'name1'.
happy_birthday('louis',age=18)          # 正常执行，可以同时使用位置参数和关键字参数
# happy_birthday(name='louis',18)       # SyntaxError: positional argument follows keyword argument
# 同时使用位置参数和关键字参数，位置参数在前，关键字参数在后

def happy_birthday1(name='Louis Wong',age=25):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 默认值参数的使用
happy_birthday1()          # 不用传参
happy_birthday1('Louis W') # 位置参数
happy_birthday1(age=27)    # 关键字传参
# happy_birthday1(19)      # TypeError: can only concatenate str (not "int") to str # 使用位置参数传参，19被传给了name
# 同时存在位置参数和默认值参数时，默认值参数放最后

# 可变参数：分为个数可变的位置参数和个数可变的关键字参数，
# 其中个数可变的位置参数是在参数前面加一颗星（*para）,para形式参数的名称，函数调用时可接收任意个数的实际参数，并放到一个元组中。
# 个数可变的关键字参数是在参数前面加两颗星（**para）,在函数调用时可接收任意多个“参数=值”形式的参数，并放到一个字典中。

def fun(*para):
    print(type(para))
    for item in para:
        print(item,end='\t')
    print()

# 个数可变的位置参数的使用
fun(10,20,30,40)              # <class 'tuple'>     10      20      30      40
fun([11,22,33,44])            # <class 'tuple'>    [11, 22, 33, 44]  # 实际上传递的是一个参数
# 在调用时，参数前加一颗星，将列表进行解包
fun(*[11,22,33,44])           # <class 'tuple'>     11      22      33      44

# 个数可变的关键字参数的使用
def fun2(**keypara):
    print(type(keypara))
    for key,value in keypara.items():
        print(key,'---',value)

fun2(name='louis',age=19,height=183)       # <class 'dict'>    name --- louis    age --- 19    height --- 183
d={'name':'louis','age':19,'height':183} 
# fun2(d)                                  # TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)                                  # <class 'dict'>    name --- louis    age --- 19    height --- 183  # 系列解包操作
