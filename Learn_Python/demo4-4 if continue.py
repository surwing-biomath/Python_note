# continue用于跳过本次循环的后续代码，而继续执行下一次循环操作，经常与if搭配使用
# while 表达式1:
#     语句块
#     if 表达式2:
#         continue

# for 循环变量 in 遍历对象:
#     语句块
#     if 表达式:
#         continue

s = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        i += 1
        continue
    s += i
    i += 1
print('sum of evens is:', s)

s = 0
for i in range(1, 101):
    if i % 2 == 1:
        continue
    s += i
print('sum of evens is:', s)

# 空语句pass：pass时Python中的保留字，在语法结构中只起到占位符作用，使语法结构完整，不报错
# 一般可用在if, for, while, 函数的定义，类的定义中

#多层循环嵌套中有if-break结构，break退出紧邻的包含if-break的循环，而继续执行外层循环
for i in 'python':
    for j in range(2):
        print(i, end='')
        if i=='h':
            break