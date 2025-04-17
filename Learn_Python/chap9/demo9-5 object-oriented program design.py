# 面向对象的三大特征：继承
# 继承：在Python中一个子类可以继承N多个父类
# 一个父类也可以拥有N多个子类
# 如果一个类没有继承任何类，那么这个类默认继承的是object类
# 子类继承父类以后，子类就拥有了（多个）父类的公共的和受保护的成员
# 继承的语法结构： 
# class 类名(父类1,父类2,...,父类N):
#    pass

class Person():                             # 默认继承了object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'我叫{self.name},现在{self.age}岁')

# Student继承Person类
class Student(Person):
    # 编写初始化的方法：
    def __init__(self, name, age, stuno):
        super().__init__(name, age)         # super调用父类的属性或方法
        self.stuno=stuno

# Doctor继承Person类
class Doctor(Person):
    # 编写初始化方法
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department=department

# 创建第一个子类对象
stu=Student('zhangsan',20,'1001')
stu.show()                                  # 我叫zhangsan,现在20岁

doctor=Doctor('lisi',42,'surgery')
doctor.show()                               # 我叫lisi,现在42岁

