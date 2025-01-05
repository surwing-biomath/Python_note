# 字符串的拼接操作
# 1，使用str.join()方法进行拼接字符串
# 2，直接拼接
# 3，使用格式化字符串进行拼接

s1='hello'
s2='world'
# (1) 使用+号进行拼接
print(s1+s2) # helloworld

#（2）使用字符串的join()方法
print(''.join([s1,s2])) # 使用空字符串拼接列表里的元素        # helloworld
print('*'.join(['hello','world','python','java','php']))    # hello*world*python*java*php
print('你好'.join(['hello','world','python','java','php'])) # hello你好world你好python你好java你好php

#（3）直接拼接
print('hello''world') # helloworld

#（4）使用格式化字符串进行拼接
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))

# 字符串的去重操作
s='helloworldhelloworldadfdfdeoodllffe'
#（1）字符串拼接及not in 
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)              # helowrdaf

#（2）使用索引+not in 
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

#（3）通过集合去重+列表排序
new_s3=set(s)
print(new_s3)         # {'l', 'a', 'r', 'o', 'w', 'd', 'h', 'f', 'e'}
lst=list(new_s3)      # ['h', 'e', 'l', 'o', 'w', 'r', 'd', 'a', 'f']
print(s.index)
lst.sort(key=s.index)
print(''.join(lst))