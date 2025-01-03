# 元组是Python中的不可变序列，用()定义，元素之间用逗号分隔，没有相关的增删改的操作
# 元组中只有一个元素的时候，逗号不能省略
# 没有相关的增删改的操作，只能使用索引获取元素，使用for循环遍历元素

# 元组的创建方式：1，元组名=(elem1, elem2, elem3, ...) 
# 2，内置函数tuple()：元组名=tuple(序列)
# 元组的删除：del 元组名

t=('hello', (10, 's'), 'world', 1, 2, 3,[1,2,3])
print(t)
t=tuple('helloworld')
print(t)
t=tuple([10, 20, 30])
print(t)

print('10在元组中是否存在：', 10 in t)
print('10在元组中出现的次数：', t.count(10))
print('最大值：', max(t))
print('最小值：', min(t))
print('元组长度：', len(t))
print('元组中元素10的索引：', t.index(10))

t=(10)
print(t, type(t)) # <class 'int'>
t=(10,) # 元组中只有一个元素的时候，逗号不能省略
print(t, type(t)) # <class 'tuple'>
t=[10]
print(t, type(t)) # <class 'list'>

# del t
# print(t) # NameError: name 't' is not defined

t=('hello', 'world', 'python')
print('t[0]:', t[0])
print('t[:3:2]:', t[:3:2])

for i in t:
    print(i)

for i in range(len(t)): # for+range()+len()遍历元组
    print(i, t[i])

for index, item in enumerate(t, start=1): # for+enumerate()遍历元组
    print(index, item)

t=[i for i in range(10)]
print(t, type(t)) # <class 'list'>
t=(i for i in range(10))
print(t, type(t)) # <class 'generator'> 
t=tuple(t)
print(t, type(t)) # <class 'tuple'>
t=tuple(i for i in range(10))
print(t, type(t)) # <class 'tuple'>

# __next__()函数取出生成器中的元素并不放回
t=(i for i in range(10))
print(t, type(t)) # <class 'generator'> 
print(t.__next__())
print(t.__next__())
print(t.__next__())
t=tuple(t)
print(t)