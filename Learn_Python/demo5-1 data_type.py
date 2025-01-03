# 序列是一个用于存储多个值的连续空间，每个值都对应一个整数的编号，称为索引；索引分为正向递增索引和反向递减索引
# 四种数据类型：列表类型、元组类型、字典类型、集合类型
# 正向递增索引范围：0 to n-1, 反向递减索引范围：-1 to -n

# 切片操作语法：序列[start:end:step]，start默认为0，end默认为n，step默认为1，
# start包含在切片中，stop不包含在切片中，start or end or step省略以后为默认值
# 步长为负数，start和end的位置互换

# 序列的相加与相乘：+表示连接，*表示重复
# 序列函数与操作符：
# in：判断元素是否在序列中: x in s, x not in s
# len()：返回序列的长度
# max()：返回序列的最大值，按照ASCII码值计算
# min()：返回序列的最小值
# s.index(x)：返回序列中第一个值为x的元素的索引
# s.count(x)：返回序列中值为x的元素的个数
s='helloworld'
print(s[::-1])
print(s[-1:-11:-1])

s='hello'
s2='world'
print(s+s2)
print(s*5)
print('-'*100)
print('h' in s, 'h' not in s)

print(max(s), min(s))
print(s.index('h'), s.count('l'))

# 列表类型：列表是一种有序的序列，是Python中内置的可变序列，
# 可以存储任意类型的数据，用[]定义，元素之间用逗号分隔
# 创建方式：1，列表名=[elem1, elem2, elem3, ...] 2，列表名=list() 3，列表名=list(序列)
# 列表的删除：del 列表名
# 列表名[索引]=新值 列表的修改：
# lst.append(x) 在列表lst最后增加一个元素
# lst.insert(index, x) 在列表lst的index位置增加一个元素
# lst.clear() 清空列表lst中所有元素
# lst.pop(index) 先将列表中指定索引的元素取出，然后再删除此元素，如果不指定索引，默认删除最后一个元素
# lst.remove(x) 删除列表中第一个值为x的元素
# lst.reverse() 将列表lst中的元素反转
# lst.copy() 复制列表lst中的元素，生成一个新列表

lst = ['hello', 'world', 1, 2, 3]
print(lst)
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)

# 列表是序列的一种，对序列的操作符、运算符、函数都适用于列表
print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3), min(lst3))
print(lst2.index('o'))
print(lst2.count('o'))

del lst2
# print(lst2) # NameError: name 'lst2' is not defined
lst[0]='hi'
print(lst)


# 列表的遍历操作
# for
for item in lst:
    print(item)

# for循环，range()函数, len()函数，根据索引进行遍历
for i in range(len(lst)):
    print(lst[i])

# 使用enumerate()函数，同时获取索引和值
for index, item in enumerate(lst):
    print(index, item) # index是序号，不是索引
# 手动修改序号起始值
for index, item in enumerate(lst, start=1):
    print(index, item)

# 列表是可变数据类型，元素可变但内存地址不变
print(lst, id(lst))
lst.append('python')
print(lst, id(lst))

lst.insert(1, 'java')
print(lst, id(lst))

lst.remove('world')
print(lst, id(lst))

print(lst.pop(1))
print(lst, id(lst))

# lst.clear()
# print(lst, id(lst))

lst.reverse()
print(lst, id(lst))

new_lst=lst.copy()
print(new_lst, id(new_lst))

lst[0]='java'
print(lst, id(lst))

# 列表排序：1，列表对象的sort()方法：lst.sort(key=None, reverse=False): key表示排序规则，reverse表示排序顺序（默认升序）
#  2，内置函数sorted()： sorted(iterable, key=None, reverse=False): iterable表示排序的对象

lst=[1, 3, 2, 5, 4]
print('原列表：', lst)
lst.sort() # 排序是在原列表上进行的，不会产生新列表
print('升序：', lst)

lst.sort(reverse=True)
print('降序：', lst)

lst2=['banana', 'apple', 'banala', 'Orange', 'Grape']
print('原列表：', lst2)
lst2.sort()
print('升序：', lst2) # 按照ASCII码值排序，大写字母在小写字母前面（大写字母ASCII值更小）
lst2.sort(reverse=True)
print('降序：', lst2)

lst2.sort(key=str.lower) # 忽略大小写排序
print('忽略大小写排序：', lst2)

lst=[1, 3, 2, 5, 4]
print('原列表：', lst)
new_lst=sorted(lst) # 产生新列表，不会改变原列表
print('升序：', new_lst)
print('原列表：', lst)

new_lst2=sorted(lst, reverse=True)
print('降序：', new_lst2)
print('原列表：', lst)

lst2=['banana', 'apple', 'banala', 'Orange', 'Grape']
new_lst3=sorted(lst2,key=str.lower)
print('原列表：', lst2)
print('忽略大小写排序：', new_lst3)

# 列表生成式语法结构：lst=[expr for item in range], expr表示表达式，item表示元素，range表示范围 
# lst=[expr for item in range if condition]，condition表示条件

import random
lst=[item for item in range(10)]
print(lst)
lst=[item for item in range(10) if item%2==0]
print(lst)
lst=[item*item for item in range(10)]
print(lst) 
lst=[random.randint(1,100) for item in range(10)]
print(lst)

# 二位列表的遍历：双层for循环
# for row in 二位列表:
#     for item in row:
#         pass
lst=[['城市', '环比', '同比'], ['北京', 102, 103], ['上海', 104, 504], ['深圳', 100, 39]]
print(lst)
for row in lst:
    for item in row:
        print(item, end='\t')
    print() # 换行

lst2=[ [j for j in range (5)] for i in range(4)] # 生成4行5列的二维列表
print(lst2)
