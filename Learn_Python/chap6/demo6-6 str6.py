# 正则表达式：特殊的一种字符串
# 1，元字符：具有特殊意义的专用字符，例如"^"和"$"分别表示匹配的开始和结束
# .  匹配任意字符（除\n）        'p\nytho\tn' ---> p,y,t,h,o,\t,n
# \w 匹配字母、数字、下划线       'python\n123'---> p,y,t,h,o,n,1,2,3
# \W 匹配非（字母、数字、下划线） 'python\n123'---> \n
# \s 匹配任意空白字符            'python\t123'---> \t
# \S 匹配任意非空白字符          'python\t123'---> p,y,t,h,o,n,1,2,3
# \d 匹配任意十进制数            'python\t123'---> 1,2,3

# 2， 限定符：用于限定匹配的次数
# ?   匹配前面的字符0次或1次        colou?r      ---> 可以匹配color或colour
# +   匹配前面的字符1次或多次       colou+r      ---> 可以匹配colour或colouu...r
# *   匹配前面的字符0次或多次       colou*r      ---> 可以匹配color或colou...r
#{n}  匹配前面的字符n次            colou{2}r     ---> 可以匹配colouur
#{n,} 匹配前面的字符至少n次         colou{2,}r   ---> 可以匹配colouur或colouuu...r
#{n,m}匹配前面的字符至少n次，至多m次 colou{2,4}r  ---> 可以匹配colouur或colouuur或colouuuur

# 3，区间字符：匹配[]中所指的字符       [.?!]          匹配标点符号点、问号、感叹号
#                                     [0-9]         匹配0,1,2,3,4,5,6,7,8,9
# 4，排除字符^:匹配不在[]中指定的字符   [^0-9]        匹配除0,1,2,3,4,5,6,7,8,9的字符
# 5，选择字符|:匹配|左右的任意字符      \d{18}|\d{15} 匹配15位身份证或18位身份证
# 6，转义字符：同Python中的转义字符     \.             将.作为普通字符使用
# 7，[\u4e00-\u9fa5]:匹配任意一个汉字
# 8，分组()：改变限定符的作用           six|fourth    匹配six或fourth
#                                     (six|four)th  匹配sixth或fourth

# re模块：Python中的内置模块，用于实现Python中的正则表达式操作
# re.match(pattern,string,flags=0)              用于从字符串的开始位置进行匹配，如果起始位置匹配成功，结果为Match对象，否则结果为None
# re.search(pattern,string,flags=0)             用于在整个字符串中搜索第一个匹配的值，如果匹配成功，结果为Match对象，否则结果为None
# re.findall(pattern,string,flags=0)            用于在整个字符串搜索所有符合正则表达式的值，结果是一个列表类型
# re.sub(pattern,repl,string,count,flags=0)     用于实现对字符串中指定子串的替换
# re.split(pattern,string,maxsplit,flags=0)     字符串中的split()方法功能相同，都是分隔字符串

import re
pattern='\d\.\d+'                  # + 匹配前面的字符1次或多次 
s='I study Python 3.13 every day'
match=re.match(pattern,s,re.I) 
print(match)                       # None
s2='3.13Python I study every day'
match2=re.match(pattern,s2)
print(match2)                      # <re.Match object; span=(0, 4), match='3.13'>

print('匹配值的起始位置：',match2.start())  # 0
print('匹配值的结束位置：',match2.end())    # 4
print('匹配区间的位置元素：',match2.span()) # (0, 4)
print('待匹配的字符串：',match2.string)     # 3.13Python I study every day
print('匹配的数据：',match2.group())       # 3.13

s3='I study Python 3.13 every day Python 2.7 I love you'
match3=re.search(pattern,s)               # 搜索第一个匹配的值
print(match3)                             # <re.Match object; span=(15, 19), match='3.13'>

s4='I study Python 3.13 every day Python 2.7 I love you'
s5='4.10Python I study every day'
s6='I study Python every day'
lst=re.findall(pattern,s4)   # ['3.13', '2.7']
lst2=re.findall(pattern,s5)  # ['4.10']
lst3=re.findall(pattern,s6)  # []
print(lst) 
print(lst2)
print(lst3)

pattern2='黑客|破解|反爬'
cmt='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
new_cmt=re.sub(pattern2,'XXX',cmt)                    # 我想学习Python，想XXX一些VIP视频，Python可以实现无底线XXX吗？
print(new_cmt)

add='https://www.baidu.com/s?wd=ysj&rsv_spt=1'
pattern3='[?|&]'
lst=re.split(pattern3,add)                            # ['https://www.baidu.com/s', 'wd=ysj', 'rsv_spt=1']
print(lst)


