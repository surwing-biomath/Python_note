# 字典类型是根据一个信息查找另一个信息的方式构成了“键值对”，它表示索引用的键和对应的值构成的成对关系。
# 与列表一样，是可变数据类型，具有增删改等一系列操作。
# 字典中的元素是无序的，通过键来访问。而且键是唯一的，值可以重复。
# 而列表中的元素是有序的，可以通过索引来访问。
# 字典中的键要求是不可变的，所以可以使用整数、浮点、字符串、元组等不可变类型作为键，而不能使用列表、字典等可变类型作为键。

# 创建字典：1，d={key1:value1,key2:value2,...} 
# 2，使用内置函数dict()创建字典，1）通过映射函数创建字典：zip(lst1,lst2)
# 2，2），d=dict(key1=value1,key2=value2,...)

# 创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key20重复，只保留最后一个，前面的被覆盖

# zip()函数：将两个列表合并成一个字典
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
d=zip(lst1,lst2) 
print(d) # <zip object at 0x0000020D2233EA40>
# print(list(d)) # [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
d=dict(d)
print(d) # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# 使用参数创建字典
d=dict(a=10,b=20,c=30) # a,b,c是键，10,20,30是值
print(d) # {'a': 10, 'b': 20, 'c': 30}

t=(10,20,30)
print({t:10}) # {(10, 20, 30): 10} # 元组是不可变的，可以作为键

lst=[10,20,30]
# print({lst:10}) # TypeError: unhashable type: 'list' # 列表是可变的，不能作为键

# 字典属于序列
print('max:',max(d)) # max: c
print('min:',min(d)) # min: a
print('len:',len(d)) # len: 3

# 字典的删除
del d
# print(d) # NameError: name 'd' is not defined

# 字典元素的取值：1，d[key] 2，d.get(key)
# 字典元素的遍历：
# 1，for element in d.items(): # 遍历出key与value的元组
# pass
# 2，for key,value in d.items() # 分别遍历出key与value
# pass

d={'hello':10,'world':20,'python':30}
print(d['hello']) # 10
print(d.get('hello')) # 10 
# 两者之间的区别：当key不存在时，d[key]会报错，而d.get(key)会返回None
# print(d['hi']) # KeyError: 'hi'
# print(d.get('hi')) # None
# print(d.get('hi','not found')) # not found

# 字典的遍历
for item in d.items():
    print(item) # key=value组成的一个元素：('hello', 10) ('world', 20) ('python', 30) 
for key,value in d.items():
    print(key,value) # 分别遍历出key与value：hello 10 world 20 python 30

# 字典的操作方法：
# 1，d.keys()：返回字典的所有键
# 2，d.values()：返回字典的所有值
# 3，d.pop(key,default)：返回相应的value,同时删除key-value对，如果key不存在，返回default
# 4，d.popitem()：随机从字典中取出一个key-value对，结果为元组类型,同时将该key-value从字典中删除
# 5，d.clear()：清空字典所有的key-value对

d={1001:'zhangsan',1002:'lisi',1003:'wangwu'}
print(d)

# 添加元素(直接赋值)
d[1004]='zhaoliu'
print(d) # {1001: 'zhangsan', 1002: 'lisi', 1003: 'wangwu', 1004: 'zhaoliu'}

# 获取所有的键
keys=d.keys()
print(keys) # dict_keys([1001, 1002, 1003, 1004])
print(list(keys)) # [1001, 1002, 1003, 1004]
print(tuple(keys)) # (1001, 1002, 1003, 1004)

# 获取所有的值
values=d.values()
print(values) # dict_values(['zhangsan', 'lisi', 'wangwu', 'zhaoliu'])
print(list(values)) # ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(tuple(values)) # ('zhangsan', 'lisi', 'wangwu', 'zhaoliu')

# 将字典中的数据转成key-value对的形式,并以元组的方式进行展现
lst=list(d.items())
print(lst) # [(1001, 'zhangsan'), (1002, 'lisi'), (1003, 'wangwu'), (1004, 'zhaoliu')]

d=dict(lst)
print(d) # {1001: 'zhangsan', 1002: 'lisi', 1003: 'wangwu', 1004: 'zhaoliu'}

# 使用pop()删除元素
print(d.pop(1001)) # zhangsan
print(d) # {1002: 'lisi', 1003: 'wangwu', 1004: 'zhaoliu'}
# print(d.pop(1001)) # KeyError: 1001

# 使用popitem()删除元素
print(d.popitem()) # (1004, 'zhaoliu')
print(d) # {1002: 'lisi', 1003: 'wangwu'}

# 使用clear()清空字典
d.clear()
print(d) # {}

# Python中一切皆对象,均有布尔值
print(bool(d)) # False # 空字典为False, 非空字典为True, 空列表、空元组、空字符串、空集合都是False

# 字典生成式
# 1，d={key:value for item in range}
# 2，d={key:value for key,value in zip(lst1,lst2)}
import random
d={item:random.randint(1,100) for item in range(10)}
print(d) # {0: 66, 1: 65, 2: 40, 3: 95, 4: 94, 5: 92, 6: 32, 7: 32, 8: 25, 9: 64}

lst=[1001,1002,1003]
lst2=['zhangsan','lisi','wangwu']
d={key:value for key,value in zip(lst,lst2)}
print(d) # {1001: 'zhangsan', 1002: 'lisi', 1003: 'wangwu'}