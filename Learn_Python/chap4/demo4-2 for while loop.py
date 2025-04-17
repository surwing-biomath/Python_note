# 循环结构：遍历循环结构for，无限循环结构while
# for 循环变量 in 遍历对象
#     语句块
# for 循环变量 in 遍历对象
#     语句块1
# else: (for 循环正常执行完毕执行else语句块)
#     语句块2
# range 内置函数，产生一个[n, m)的整数序列
for i in range(100, 1000):
    a = i%10
    b = i//10%10
    c = i//100
    if i == a**3+b**3+c**3:
        print(i, 'qualifies')

# while循环四个步骤：1，初始化变量；2，条件判断；3，语句块；4，改变变量
# while 表达式:
#     语句块
# while 表达式:
#     语句块1
# else:
#     语句块2

# （1）：初始化变量
answer = input('do we need to have class?y/n')
# （2）：条件判断
while answer == 'y':
# （3）：语句块
    print('good good study, day day up')
# （4）：改变变量
    answer = input('do we need to have class?y/n')

s = 0
i = 1
while i <= 100:
    s += i
    i += 1
else:
    print('the sum bwt 1 and 100 is', s)

i = 0 # 初始化
while i < 3: # 判断
    name = input('input name')
    pwd = input('input password')
    if name == 'louis' and pwd == '1': # if--else-- 结构两个语句块都有改变变量步骤
        print('correct password')
        i = 8 # 改变
    else:
        if i<2:
            print('incorrect password, you have', 2-i, 'tries')
        i+=1 # 改变
if i == 3:
    print('you have tried three times and you have no chance now')

# 嵌套循环：循环结构嵌套循环结构，建议不要嵌套超过三层（总循环次数=\prod_{循环嵌套数}每个循环循环数目）
# 嵌套循环经常用于输出一些图形，例如长方形、三角形、菱形等

k = eval(input('input k: '))
if k == 0:
    for i in range(3):
        for j in range(4):
            print('*', end='')
        print() # 空的print 作用换行
elif k == 1:
    for i in range(5):
        for j in range(i+1):
            print('*',end='')
        print()
elif k == 2:
    for i in range(5):
        for j in range(5-i):
            print('*', end='')
        print()
elif k == 3:
    for i in range(5):
        for j in range(9):
            if j <= 3-i:
                print(' ', end='')
            elif j in range(4-i, 5+i):
                print('*', end='')
            else:
                print(' ',end='')
        print()
elif k == 4:
    row = eval(input('input row number:'))
    while row%2 == 0:
        print('input row again')
        row = eval(input('input row number:'))
    for i in range(1, (row+1)//2+1):
        for j in range(1, (row+1)//2+1-i):
            print(' ', end='')
        for w in range(1,2*i):
                print('*', end='')
        print()
    for i in range(1, (row+1)//2):
        for j in range(1, i+1):
            print(' ', end='')
        for w in range(1, row-2*i+1):
            print('*', end='')
        print()

elif k == 5:
    row = eval(input('input row number:'))
    while row % 2 == 0:
        print('input row again')
        row = eval(input('input row number:'))
    for i in range(1, (row+1)//2+1):
        for j in range(1, (row+1)//2+1-i):
            print(' ', end='')
        for w in range(1,2*i):
            if w == 1 or w == 2*i-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    for i in range(1, (row+1)//2):
        for j in range(1, i+1):
            print(' ', end='')
        for w in range(1, row-2*i+1):
            if w == 1 or w == row-2*i:
                print('*', end='')
            else:
                print(' ', end='')
        print()





