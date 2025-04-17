# 继承：子类方法名字与父类方法名字完全相同，而去修改方法的方法体，即方法体的重新编写就为方法重写
# 方法重写：子类继承了父类就拥有了父类中的公有成员和受保护的成员
# 父类的方法并不能完全适合子类的需求和要求，这个时候子类就可以重写父类的方法
# 子类在重写父类的方法时，要求方法的名称必须与父类方法的名称相同，在子类重写后的方法中可以通过super().xxx()调用父类中的方法

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

    def show(self):
        # 调用父类中的方法
        super().show()
        print(f'我来自xxx大学，我的学号是{self.stuno}')

# Doctor继承Person类
class Doctor(Person):
    # 编写初始化方法
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department=department
    
    def show(self):
        # super().show()                    # 不调用父类中show方法，而去完全重写show()方法
        print(f'大家好，我的名字是{self.name}，我今年{self.age}岁，我的工作科室是{self.department}')


# 创建第一个子类对象
stu=Student('zhangsan',20,'1001')
stu.show()                                  # 我叫zhangsan,现在20岁

doctor=Doctor('lisi',42,'surgery')
doctor.show()                               # 我叫lisi,现在42岁