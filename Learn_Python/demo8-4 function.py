# 匿名函数lambda：是指没有名字的函数，这种函数只能使用一次，一般是在函数的函数体只有一句代码且只有一个返回值时，可以使用匿名函数来简化
# 语法结构：result=lambda 参数列表:表达式

def calc(a,b):
    return a+b
print(calc(10,20))

# 匿名函数
s=lambda a,b:a+b   # s表示的是一个匿名函数
print(type(s))     # <class 'function'>
# 调用匿名函数
print(s(10,20))    # 30
print('-'*50)

# 列表的正常取值操作
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i],end='\t')
print('-'*50)

# 使用匿名函数进行列表取值
lst=[10,20,30,40,50]
for i in range(len(lst)):
    result=lambda x:x[i]   # 匿名函数的功能是根据索引取值，result的类型是function，x是形式参数
    print(result(lst))     # lst是实际参数
print('-'*50)

# 使用匿名函数对列表进行排序，排序的规则是按照成绩降序排列
student_score=[
    {'name':'Louis','score':98},
    {'name':'Wog','score':95},
    {'name':'Kim','score':100},
    {'name':'Turing','score':65}
]
student_score.sort(key=lambda x:x.get('score'),reverse=True)
print(student_score)
