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

# 根据类的“图纸”可以创建出N多个
stu1=Student('louis wong',18)
stu2=Student('zhansan',25)
stu3=Student('lisi',22)
stu4=Student('Marry',20)

Student.school='Python education'

# 将学生对象存储在列表中
lst=[stu1,stu2,stu3,stu4]           # 列表中的元素是Student类型的对象
for item in lst:                    # item是列表中的元素，是Student类型的对象
    item.show()                     # 对象名打点调用实例方法


# 动态绑定属性和方法：每个对象的属性名称相同，但属性值不同，可以为某个对象绑定独有的属性或方法

# 创建两个Student类型的对象
stu=Student('louis Wog',18)
stu2=Student('xhans',20)
print(stu.name,stu.age)                  # louis Wog 18
print(stu2.name,stu2.age)                # xhans 20

# 为stu2动态绑定一个实例属性
stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)   # xhans 20 男
# print(stu.gender)                     # AttributeError: 'Student' object has no attribute 'gender'

# 动态绑定方法
def introduce():
    print('我是一个函数，被动态绑定成对象stu2的方法')
stu2.fun=introduce # 函数的赋值
# fun就是对象stu2的方法
# 调用
stu2.fun()

