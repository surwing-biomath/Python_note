import random
# def get_max(lst):
#     x=lst[0]
#     for i in range(1,len(lst)):
#         if lst[i]>x:
#             x=lst[i]
#     return x

# # 调用
# lst=[random.randint(1,100) for item in range(10)]
# print(lst,get_max(lst))


# def get_digit(x):
#     s=0
#     lst=[]
#     for item in x:
#         if item.isdigit():
#             lst.append(int(item))    
#     s=sum(lst)
#     return lst,s

# s=input('请输入一个字符串：')
# lst,x=get_digit(s)
# print('提取的数字列表为：',lst)
# print('累加和为：',x)


# def lower_upper(x):
#     lst=[]
#     for item in x:
#         if 'A'<=item<='Z':
#             lst.append(chr(ord(item)+32))
#         elif 'a'<=item<='z':
#             lst.append(chr(ord(item)-32))
#         else:
#             lst.append(item)

#     return ''.join(lst)

# s=input('请输入一个字符串：')
# new_s=lower_upper(s)
# print(new_s)


def get_find(s,lst):
    for item in lst:
        if s==item:
            return True
    return False

lst=['hello','world','python']
s=input('请输入您要判断的字符串：')
result=get_find(s,lst)
print('存在' if result else '不存在')           # if...else的简写，三元运算符（三目运算符，条件表达式）