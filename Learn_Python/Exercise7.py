# class Circle():
#     def __init__(self,r):
#         self.r=r

#     def get_area(self):
#         return 3.14*self.r**2
    
#     def get_perimeter(self):
#         return 2*3.14*self.r
    
# r=eval(input('请输入圆的半径：'))
# c=Circle(r)
# area=c.get_area()
# perimeter=c.get_perimeter()
# print('圆的面积为：',area,'圆的周长为：',perimeter)


# class Student():
#     def __init__(self,name,age,gender,score):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.score=score

#     def info(self):
#         print(self.name,self.age,self.gender,self.score)

# print('请输入五位学生信息：（姓名#年龄#性别#成绩）')
# lst=[]
# for i in range(1,6):
#     s=input(f'请输入第{i}位学生信息及成绩')
#     s_lst=s.split('#')
#     stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
#     lst.append(stu)

# for item in lst:
#     item.info()


# class Instrument():
#     def make_sound(self):
#         pass

# class Erhu(Instrument):
#     def make_sound(self):
#         print('二胡在弹奏')

# class Piano(Instrument):
#     def make_sound(self):
#         print('钢琴在弹奏')

# class Violin(Instrument):
#     def make_sound(self):
#         print('小提琴在弹奏')

# def play(obj):
#     obj.make_sound()

# er=Erhu()
# piano=Piano()
# vio=Violin()

# play(er)
# play(piano)
# play(vio)


# class Car(object):
#     def __init__(self,type,no):
#         self.type=type
#         self.no=no

#     def start(self):
#         print('我是车，我能启动')
#     def stop(self):
#         print('我是车，我能停止')

# class Taxi(Car):
#     def __init__(self, type, no, company):
#         super().__init__(type, no)
#         self.company=company

#     def start(self):
#         print('乘客您好！')
#         print(f'我是{self.company}公司出租车，我的车牌是{self.no}，您要去哪里？')

#     def stop(self):
#         print('目的地到了，请您扫码付款，欢迎下次乘坐')

# class FamilyCar(Car):
#     def __init__(self, type, no, name):
#         super().__init__(type, no)
#         self.name=name
    
#     def start(self):
#         print(f'我是{self.name}，我的轿车我做主')

#     def stop(self):
#         print(f'目的地到了，我们去玩吧！')

# taxi=Taxi('上海大众','京A8888','长城')
# taxi.start()
# taxi.stop()
# print('-'*40)

# famcar=FamilyCar('广汽丰田','京B6666','武大郎')
# famcar.start()
# famcar.stop()