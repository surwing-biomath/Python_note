class FatherA():
    def __init__(self,name):
        self.name=name
    
    def showA(self):
        print('父类A中的方法')

class FatherB():
    def __init__(self,age):
        self.age=age

    def showB(self):
        print('父类B中的方法')

class Son(FatherA,FatherB):
    def __init__(self, name, age, gender):
        # 需要调用两个父类的初始化方法
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)
        self.gender=gender

son=Son('zhansan',20,'男')
son.showA()                                 # 父类A中的方法
son.showB()                                 # 父类B中的方法

