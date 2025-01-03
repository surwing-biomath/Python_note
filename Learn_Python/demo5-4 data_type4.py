# Python中的集合与数学中的集合概念一致, 集合中的元素是无序的不重复的元素序列
# 集合只能存储不可变数据类型, 不能存储可变数据类型
# 集合使用{}定义, 元素之间使用逗号分隔
# 集合与列表,字典一样都是可变数据类型

# 创建集合
# 1, 使用{}创建集合: s={ele1, ele2, ele3, ...}
# 2, 使用内置函数set()创建集合: s=set(可迭代对象)
# 集合的删除: del 集合名

s={1, 2, 3, 4, 5}
print(s, type(s))
# 集合只能存储不可变数据类型
# s={[10,20],[30,40]} # TypeError: unhashable type: 'list'

s=set()
print(s) # set()
s={} # 创建的是集合还是字典?
print(s, type(s)) # {} <class 'dict'>

s=set('helloworld')
print(s) # {'d', 'l', 'o', 'r', 'w', 'h', 'e'} # 集合中的元素是无序的,不重复的元素序列

s2=set([10, 20, 30, 40])
print(s2) # {40, 10, 20, 30}

s3=set(range(10))
print(s3) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# 集合是序列中的一种
print('max:', max(s3)) # 9
print('min:', min(s3)) # 0
print('sum:', sum(s3)) # 45
print('len:', len(s3)) # 10

print('9 in s3:', 9 in s3) # True
print('9 not in s3:', 9 not in s3) # False

# 集合的运算
# 交集: A&B
# 并集: A|B
# 差集: A-B
# 对称差集: A^B
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print('s1&s2:', s1&s2) # {4, 5}
print('s1|s2:', s1|s2) # {1, 2, 3, 4, 5, 6, 7, 8}
print('s1-s2:', s1-s2) # {1, 2, 3} 
print('s1^s2:', s1^s2) # {1, 2, 3, 6, 7, 8}

# 集合操作:
# s.add(x): 向集合中添加元素x
# s.update(x): 向集合中添加多个元素
# s.remove(x): 从集合中删除元素x, 如果元素不存在, 抛出KeyError异常
# s.discard(x): 从集合中删除元素x, 如果元素不存在, 不抛出异常
# s.clear(): 清空集合

s={10, 20, 30}
s.add(40)
print(s) # {40, 10, 20, 30}
s.update([50, 60, 70])
print(s) # {70, 40, 10, 50, 20, 60, 30}
s.remove(70)
print(s) # {40, 10, 50, 20, 60, 30}
# s.remove(80) # KeyError: 80
s.discard(80)
print(s) # {40, 10, 50, 20, 60, 30}
s.clear()
print(s) # set()

# 集合的遍历
s={10, 20, 30, 40}
for ele in s:
    print(ele)
for index, item in enumerate(s): # index指的是序号,而不是索引,因为集合是无序的
    print(index, item)

# 集合的生成式
s={i for i in range(10)}
print(s) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

s={i for i in range(10) if i%2==1}
print(s) # {1, 3, 5, 7, 9}

# 数据类型 | 元素是否可重复 | 是否可变 | 是否有序 | 定义符号 
# 列表list | 可重复        | 可变     | 有序    | []
# 元组tuple| 可重复        | 不可变   | 有序    | ()
# 字典dict | key不可重复   | 可变     | 无序    | {key:value}
#          | value可重复   |         |         |
# 集合set  | 不可重复      | 可变     | 无序    | {}或set()

# Python3.11新特性:
# 1, 结构模式匹配:
#    使用match语句进行模式匹配, 用于替代if-elif-else语句
# match data:
#     case {}:
#         pass
#     case []:
#         pass
#     case ():
#         pass
#     case _:
#         pass

# data=eval(input('请输入一个数据:'))
# match data:
#     case {'name':'zhangsan', 'age':20}:
#         print('输入的是字典')
#     case [10,20,30]:
#         print('输入的是列表')
#     case (10,20,40):
#         print('输入的是元组')
#     case _:
#         print('其他')

# 2, 字符合并运算符 |:
#    使用|符号可以将两个字符串合并为一个字符串
d1={'name':'zhangsan'}
d2={'age':20}
d3=d1|d2
print(d3) # {'name': 'zhangsan', 'age': 20}

# 3, 同步迭代:
# match data1, data2:
#     case data1, data2:
#         pass

fruit={'apple', 'banana', 'orange', 'grape', 'pear'}
counts={10, 20, 30, 40, 50}
for f, c in zip(fruit, counts):
    match f, c:
        case 'apple', 10:
            print('10个苹果')
        case 'banana', 20:
            print('20个香蕉')
        case 'orange', 30:
            print('30个橙子')
        case 'grape', 40:
            print('40个葡萄')
        case 'pear', 50:
            print('50个梨')
# When you use zip(fruit, counts), Python pairs elements based on their positions in the sets. 
# However, since sets are unordered, the elements in fruit and counts might not align in the order you expect.
print('-'*50)
fruit=['apple', 'banana', 'orange', 'grape', 'pear']
counts=[10, 20, 30, 40, 50]
for f, c in zip(fruit, counts):
    match f, c:
        case 'apple', 10:
            print('10个苹果')
        case 'banana', 20:
            print('20个香蕉')
        case 'orange', 30:
            print('30个橙子')
        case 'grape', 40:
            print('40个葡萄')
        case 'pear', 50:
            print('50个梨')

d={'a':10, 'b':20, 'c':30, 'd':40}
d2=d
print(id(d), id(d2)) # 140707366004352 140707366004352
d['b']=100 # d2['b']同时改变,因为d2和d指向同一个内存空间
print(d['b'], d2['b']) # 200