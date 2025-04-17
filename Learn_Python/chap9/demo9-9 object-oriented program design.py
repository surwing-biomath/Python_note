# object类：所有类直接或间接的父类
# 所有类都拥有object类的属性和方法
# object类中的特殊的方法及功能描述：
# __new__():            由系统调用，用于创建对象
# __init__():           创建对象（类实例化）时自动调用，用于初始化对象属性值，给实例属性赋值
# __str__():            对象的描述，返回值是str类型，默认输出对象的内存地址。

class Person1():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f'大家好，我叫{self.name}，我今年{self.age}岁')

# 创建Person类的对象
per1=Person1('louis Wog',20)                # 创建对象的时候会自动调用__init__()方法
print(dir(per1))                            # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', 
                                            # '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
                                            # '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', 
                                            # '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'show']

print(per1)                                 # <__main__.Person1 object at 0x000001BC58746900>  # 自动调用了__str__方法

# 重写父类的__str__()方法
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # 方法重写
    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'   # 返回值是一个字符串

# 创建Person类对象
per=Person('zhangsan',20)                               
print(per)                                              # 这是一个人类，具有name和age两个实例属性       # 不再是内存地址，而是__str__方法中的内容。直接输出对象名，实际上是调用__str__方法
print(per.__str__())                                    # 这是一个人类，具有name和age两个实例属性       # 手动调用
