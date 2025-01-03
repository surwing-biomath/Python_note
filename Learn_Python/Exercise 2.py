# fp = open('text.txt', 'w')
# print('人生苦短，我用Python', file=fp)
# fp.close()
#
# name = input('请输入您的姓名：')
# age = input('请输入您的年龄：')
# motto = input('请输入您的座右铭：')
# print('---自我介绍---')
# print('姓名：'+name)
# print('年龄：'+age)
# print('座右铭：'+motto)

# print('-'*40)
# num = eval(input('请输入一个四位整数：'))
# a = num//1000
# b = (num-a*1000)//100
# c = (num-a*1000-b*100)//10
# d = (num-a*1000-b*100-c*10)
# print('个位数字为：', d)
# print('十位数字为：', c)
# print('百位数字为：', b)
# print('千位数字为：', a)

# print('-'*40)
# num = int(input('请输入一个整数：'))
# print('个位数字为：', num%10)
# print('十位数字为：', num//10%10)
# print('百位数字为：', num//100%10)
# print('千位数字为：', num//1000)

# print('-'*40)
# num = input('请输入一个四位整数：')
# print('个位数字为：', num[3])
# print('十位数字为：', num[2])
# print('百位数字为：', num[1])
# print('千位数字为：', num[0])

# print('-'*40)
# father = float(input('父亲身高：'))
# mother = float(input('母亲身高：'))
# print('儿子身高：', (father+mother)*0.54)

# year = eval(input('input year:'))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(year, '闰年')
# else:
#     print(year, '平年')

# # 初始化变量
# answer = 'y'
# # 条件判断
# while answer=='y':
#     print('------欢迎使用10086查询功能------')
#     print('1.查询当前余额')
#     print('2.查询当前剩余流量')
#     print('3.查询当前剩余通话时长')
#     print('0.退出系统')
#     choice=input('请输入要进行的操作:')
#     if choice=='1':
#         print('当前余额为2元')
#     elif choice=='2':
#         print('当前剩余流量为3G')
#     elif choice=='3':
#         print('当前剩余通话时长为5min')
#     elif choice=='0':
#         print('程序退出，谢谢使用')
#         break
#     else:
#         print('输入有误，重新输入')
# # 改变变量
#     answer = input('是否继续操作？y/n')
# else: # while-else没有遇到break退出
#     print('程序退出')

# for i in range(9):
#     for j in range(i+1):
#         print(str(j+1)+'*'+str(i+1)+'='+str((j+1)*(i+1)), end='\t')
#     print()

import random
rand=random.randint(1,100)
print('guess a random number btw 1 and 100, and you have ten times to try')
count=1
while count<=10:
    a=eval(input('input guess:'))
    if a==rand:
        print('correct answer')
        break
    elif a>rand:
        print('the number is smaller')
    else:
        print('the number is bigger')
    count += 1
if count<=3:
    print('you are so smart, guessed', count, 'times')
elif count<=6:
    print('fairly good, guessed', count, 'times')
elif count<=10:
    print('you have tried too many times and the time is', count)
elif count>10:
    print('you stupid guy have no chances to try')



