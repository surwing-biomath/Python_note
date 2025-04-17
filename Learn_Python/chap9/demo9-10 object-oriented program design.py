# 运算符也是通过调用特殊方法实现的
# +             __add__()                       执行加法运算       
# -             __sub__()                       执行减法运算
# <,<=,==       __lt__(),__le__(),__eq__()      执行比较运算
# >,>=,!=       __gt__(),__ge__(),__ne__()      执行比较运算
# *,/           __mul__(),__truediv__()         执行乘法、非整除运算
# %,//          __mod__(),__floordiv__()        执行取余、整除运算
# **            __pow__()                       执行幂运算

a=10
b=20
print(dir(a))                           # Python中一切皆对象        # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
# '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', 
# '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', 
# '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
# 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
print(a.__add__(b))                     # 30
print(a.__sub__(b))                     # -10
print(f'{a}<{b}吗？',a.__lt__(b))       # 10<20吗？ True
print(f'{a}<={b}吗？',a.__le__(b))      # 10<=20吗？ True
print(f'{a}=={b}吗？',a.__eq__(b))      # 10==20吗？ False
print(f'{a}>{b}吗？',a.__gt__(b))       # 10>20吗？ False
print(f'{a}>={b}吗？',a.__ge__(b))      # 10>=20吗？ False
print(f'{a}!={b}吗？',a.__ne__(b))      # 10!=20吗？ True、
print('-'*50)
print(a.__mul__(b))                     # 200
print(a.__truediv__(b))                 # 0.5
print(a.__mod__(b))                     # 10
print(a.__floordiv__(b))                # 0
print(a.__pow__(2))                     # 100
print('-'*50)

# 特殊属性
# obj.__dict__                          # 对象的属性字典
# obj.__class__                         # 对象所属的类
# obj.__bases__                         # 类的父类元组
# obj.__base__                          # 类的父类
# obj.__mro__                           # 类的层次结构
# obj.__subclasses__()                  # 类的子类列表

class A():
    pass

class B():
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

# 创建类的对象
a=A()
b=B()
c=C('louis Wog',20)

print('对象a的属性字典：',a.__dict__)               # 对象a的属性字典： {}
print('对象b的属性字典：',b.__dict__)               # 对象b的属性字典： {}
print('对象c的属性字典：',c.__dict__)               # 对象c的属性字典： {'name': 'louis Wog', 'age': 20}
print('-'*50)

print('对象a所属的类：',a.__class__)                # 对象a所属的类： <class '__main__.A'>
print('对象b所属的类：',b.__class__)                # 对象b所属的类： <class '__main__.B'>
print('对象c所属的类：',c.__class__)                # 对象c所属的类： <class '__main__.C'>
print('-'*50)

print('A类的父类元组：',A.__bases__)                # A类的父类元组： (<class 'object'>,)
print('B类的父类元组：',B.__bases__)                # B类的父类元组： (<class 'object'>,)
print('C类的父类元组：',C.__bases__)                # C类的父类元组： (<class '__main__.A'>, <class '__main__.B'>)
print('-'*50)

print('A类的父类：',A.__base__)                     # A类的父类： <class 'object'>
print('B类的父类：',B.__base__)                     # B类的父类： <class 'object'>
print('C类的父类：',C.__base__)                     # C类的父类： <class '__main__.A'>      # 如果继承了多个父类，结果只显示第一个父类
print('-'*50)

print('A类的层次结构：',A.__mro__)                  # A类的层次结构： (<class '__main__.A'>, <class 'object'>)
print('B类的层次结构：',B.__mro__)                  # B类的层次结构： (<class '__main__.B'>, <class 'object'>)
print('C类的层次结构：',C.__mro__)                  # C类的层次结构： (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print('-'*50)                                      # C类继承了A类、B类，间接继承了object类

print('A类的子类列表：',A.__subclasses__())         # A类的子类列表： [<class '__main__.C'>]
print('B类的子类列表：',B.__subclasses__())         # B类的子类列表： [<class '__main__.C'>]
print('C类的子类列表：',C.__subclasses__())         # C类的子类列表： []