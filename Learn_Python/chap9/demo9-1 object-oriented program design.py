# 两大编程思想：面向过程和面向对象
# 面向过程：功能上的封装，典型代表：C
# 面向对象：属性和行为上的封装，典型代表：Python,Java
# 事物比较简单，可以用线性的思维解决的时候使用面向过程；事物比较复杂，使用简单的线性思维无法解决的时候使用面向对象
# 面向过程和面向对象都是解决实际问题的一种思维方式
# 二者相辅相成，并不是独立的；解决复杂问题，通过面向对象方式便于我们从宏观上把握事物之间复杂的关系，方便我们分析整个系统，具体到微观操作，仍然使用面向过程方式来处理

# 面向对象：类和对象
# 类：是由N多个对象抽取出“像”的属性和行为从而归纳总结出来的一种类别
# 类相当于图纸，抽象的模板，对象是具体的实例

a=10
b=9.8
c='hello'
print(type(a))                      # <class 'int'>
print(type(b))                      # <class 'float'>
print(type(c))                      # <class 'str'>

# 自定义数据类型的语法结构为：(类名首字母大写)
# class 类名():
#     pass
# 创建对象的语法格式为：
# 对象名=类名()

# 编写一个Person类型
class Person():
    pass
class Cat():
    pass
class Dog():
    pass
class Student():
    pass

# 创建类的对象
# 对象名=类名()

# 创建一个Person类型的对象
per=Person()                        # per就是Person类型的对象
c=Cat()                             # c就是Cat类型的对象
d=Dog()                             # d就是Dog类型的对象
stu=Student()                       # stu就是Student类型的对象
print(type(per))                    # <class '__main__.Person'>
print(type(c))                      # <class '__main__.Cat'>
print(type(d))                      # <class '__main__.Dog'>
print(type(stu))                    # <class '__main__.Student'>

# 类的组成：类属性、实例属性、实例方法、静态方法、类方法
# 类属性：直接定义在类中，方法外的变量
# 实例属性：定义在__init__方法中，使用self打点的变量
# 实例方法：定义在类中的函数，而且自带参数self
# 静态方法：使用装饰器@staticmethod修饰的方法
# 类方法：使用装饰器@classmethod修饰的方法

class Student():
    # 类属性：定义在类中，方法外的变量
    school='北京xxxx教育'
    
    # 初始化方法
    def __init__(self,louis,age):   # louis,age是方法的参数，是局部变量，louis,age的作用域是整个__init__方法
        self.name=louis             # =左侧是实例属性，louis是局部变量，将局部变量的值louis赋值给实例属性self.name
        self.age=age                # 实例属性的名称和局部变量的名称可以相同

    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫{self.name}，今年{self.age}岁')
    
    # 静态方法：使用装饰器@staticmethod修饰的方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')
    
    # 类方法：使用装饰器@classmethod修饰的方法
    @classmethod
    def cm(cls):   # cls--->class的简写
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

# 创建类的对象
stu=Student('Louis Wong',18) # 传了两个参数，因为__init__方法中，有两个形式参数，self是自带的参数，无需手动传入
# 实例属性，使用对象名进行打点调用
print(stu.name,stu.age)
# 类属性，直接使用类名，打点调用
print(Student.school)

# 实例方法，使用对象名进行打点调用
stu.show()

# 类方法，@classmethod进行修饰的方法，直接使用类名打点调用
Student.cm()

# 静态方法，@staticmethod进行修饰的方法，直接使用类名打点调用
Student.sm()

# 类属性、静态方法、类方法，使用类名进行打点调用；实例属性、实例方法，使用对象名打点调用

