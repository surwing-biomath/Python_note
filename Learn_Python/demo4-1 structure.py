# if True (bool value of any object), then execuate; false, then skip
# 执行if语句时，如果语句块只有一句代码，可以直接将语句块写在冒号后面
x = input('input a string:')
if x:
    print('input non-empty string')
if not x:print('input empty string')

x = eval(input('True or False:'))
if x:
    print('x is True')
if not x:print('x is False')

# if 表达式1:
#     语句块1
# else:
#     语句块2
# 每个代码块只有一句时可以简化
x = input('input a string:')
if x:
    print('input non-empty string')
else:
    print('input empty string')

print('input non-empty string' if x else 'input empty string')

# if 表达式1:
#     语句块1
# elif 表达式2:
#     语句块2
# elif 表达式n:
#     语句块n
# else: (optional)
#     语句块n+1

score = eval(input('input score:'))
if score < 0 or score > 100:
    print('invalid score')
elif 0 <= score <= 20:
    print('your score is in E range')
elif 20 < score <= 40:
    print('your score is in D range')
elif 40 < score <= 60:
    print('your score is in C range')
elif 60 < score <=80:
    print('your score is in B range')
else:
    print('your score is in A range')

# 嵌套结构：内层的分支结构作为外层分支结构的语句块使用
# 模型匹配
score = input('input grade:')
match score:
    case 'A':
        print('excellent')
    case 'B':
        print('fair')
    case 'C':
        print('pass')
    case 'D':
        print('fail')
