# 面向对象的三大特征
# 1，封装：隐藏内部细节，对外提供访问属性和方法的操作方式，保证数据的安全性
# 2，继承：是在函数调用时，使用“形参名称=值”的方式进行传参，传递参数顺序可以与定义时参数的顺序不同
# 3，多态，是在函数定义时，直接对形式参数进行赋值，在调用时如果该参数不传值，将使用默认值，如果该参数传值，则使用传递的值
# 封装：权限控制：是通过对属性和方法添加单下划线、双下划线以及首位双下划线来实现
# 单下划线开头：以单下划线开头的属性或方法表示protected受保护的成员，这类成员被视为仅供内部使用，允许类本身和子类进行访问，但实际上它可以被外部代码访问。
# 双下划线开头：表示private私有的成员，这类成员只允许定义该属性或方法的类本身进行访问
# 首位双下划线：一般表示特殊的方法

# 权限控制
class Student():
    # 首位双下划线：
    def __init__(self,name,age,gender):
        self._name=name             # self._name受保护的，只能本类和子类访问
        self.__age=age              # self.__age表示私有的，只能类本身去访问
        self.gender=gender          # self.gender普通的实例属性，类的内部、外部、以及子类都可以访问

    def _fun1(self):                # 受保护的
        print('子类及本身可以访问')

    def __fun2(self):               # 私有的
        print('只有定义的类可以访问')

    def show(self):                 # 普通的实例方法
        self._fun1()                # 类本身访问受保护的方法
        self.__fun2()               # 类本身访问私有方法
        print(self._name)           # 受保护的实例属性
        print(self.__age)           # 私有的实例属性

# 创建一个学生类对象
stu=Student('louis Wog',20,'男')
# 类的外部
print(stu._name)                    # louis Wog
# print(stu.__age)                  # AttributeError: 'Student' object has no attribute '__age'.

# 调用受保护的实例方法
stu._fun1()                         # 子类及本身可以访问
# 私有方法
# stu.__fun2()                      # AttributeError: 'Student' object has no attribute '__fun2'.

# 私有的实例属性和方法真的不能访问吗？
print(stu._Student__age)            # 为什么可以这样访问呢？但非常不推荐这种方法访问
stu._Student__fun2()                # 

print(dir(stu))                     # ['_Student__age', '_Student__fun2', '__class__', '__delattr__', '__dict__', '__dir__', 
# '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_fun1', '_name', 'gender', 'show']

