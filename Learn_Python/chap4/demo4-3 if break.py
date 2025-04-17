# break用于跳出循环结构，通常与if搭配使用
# while 表达式1:
#     语句块1
#     if 表达式2:
#         break

# for 循环变量 in 遍历对象:
#     语句块
#     if 表达式:
#         break

s = 0
i = 1
while i < 11:
    s += i
    if s > 20:
        print('smallest i such that sum > 20 is', i)
        break
    i += 1

i = 0
while i < 3:
    name = input('input name')
    pwd = input('input password')
    if name == '1' and pwd == '1':
        print('correct password')
        break
    else:
        if i < 2:
            print('incorrect password, you have', 2 - i, 'chances left')
    i += 1
else:
    print('three tries with wrong password')

for i in range(3):
    name = input('input name')
    pwd = input('input password')
    if name == '1' and pwd == '1':
        print('correct password')
        break
    else:
        if i < 2:
            print('incorrect password, you have', 2 - i, 'chances left')
else:
    print('three tries with wrong password')
