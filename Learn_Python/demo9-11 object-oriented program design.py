# 类的深拷贝与浅拷贝
# 变量的赋值：只是形成两个变量，实际上还是指向同一个对象
# 浅拷贝：拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
# 深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同

class CPU():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu=CPU()
disk=Disk()
com=Computer(cpu,disk)

# 变量（对象）的赋值
com1=com
print(com)                                              # <__main__.Computer object at 0x00000219F69A6BA0>
print(com1)                                             # <__main__.Computer object at 0x00000219F69A6BA0>
print('子对象的内存地址：',com.cpu,com.disk)              # <__main__.CPU object at 0x00000219F69A6900> <__main__.Disk object at 0x00000219F69A6A50>
print('子对象的内存地址：',com1.cpu,com1.disk)            # <__main__.CPU object at 0x00000219F69A6900> <__main__.Disk object at 0x00000219F69A6A50>
print('-'*50)

# 类对象的浅拷贝
import copy
com2=copy.copy(com)                                     # com2是新产生的对象，com2的子对象cpu,disk不变
print(com)                                              # <__main__.Computer object at 0x00000219F69A6BA0>
print(com2)                                             # <__main__.Computer object at 0x00000219F6C116D0>
print('子对象的内存地址：',com.cpu,com.disk)              # <__main__.CPU object at 0x00000219F69A6900> <__main__.Disk object at 0x00000219F69A6A50>
print('子对象的内存地址：',com2.cpu,com2.disk)            # <__main__.CPU object at 0x00000219F69A6900> <__main__.Disk object at 0x00000219F69A6A50>
print('-'*50)

# 类对象的深拷贝
import copy
com3=copy.deepcopy(com)                                 # com3是新产生的对象，com3的子对象cpu,disk也会重新创建
print(com)                                              # <__main__.Computer object at 0x00000219F69A6BA0>
print(com3)                                             # <__main__.Computer object at 0x00000219F6C11810>
print('子对象的内存地址：',com.cpu,com.disk)              # <__main__.CPU object at 0x00000219F69A6900> <__main__.Disk object at 0x00000219F69A6A50>
print('子对象的内存地址：',com3.cpu,com3.disk)            # <__main__.CPU object at 0x00000219F6C11950> <__main__.Disk object at 0x00000219F6C11A90>