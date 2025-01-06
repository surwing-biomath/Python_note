# 变量的作用域：指变量起作用的范围，根据范围作用的大小可分为局部变量和全局变量
# 局部变量：在函数定义处的参数和函数内部定义的变量，
# 作用范围：仅在函数内部，函数执行结束，局部变量的生命周期也结束
# 全局变量：在函数外定义的变量或函数内部使用global关键字修饰的变量，
# 作用范围：作用于整个程序，程序运行结束，全局变量的生命周期才结束

def calc(a,b):
    s=a+b
    return s

# print(a,b,s)     # NameError: name 'a' is not defined # a,b是函数的参数，参数是局部变量，s是函数中定义的变量，也是局部变量

result=calc(10,20)
print(result)

a=100                   # 全局变量
def calc2(x,y):
    return a+x+y
print(a,calc2(10,20))   # 100 130 # 全局变量可以直接在函数内部使用
print('-'*50)

def calc3(x,y):
    a=200               # 局部变量a与全局变量的名称相同
    return a+x+y        # 当局部变量与全局变量的名称相同时，局部变量优先级更高
print(a,calc3(10,20))   # 100 230
print('-'*50)

def calc4(x,y):
    global s            # s是在函数中定义的变量，但是使用了global关键字声明，这个变量s变成了全局变量
    s=300               # 声明和赋值，必须是分开执行
    return s+x+y
print(calc4(10,20),s)   # 330 300
