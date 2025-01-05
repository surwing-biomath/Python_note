# 字符串是Python中不可变数据类型
# str.lower() 将str字符串全部转成小写字母，结果为一个新的字符串
# str.upper() 将str字符串全部转成大写字母，结果为一个新的字符串
# str.split(sep=None) 将str按照指定的分隔符sep进行分割，结果为列表类型
# str.count(sub) 结果为sub这个字符串在str中出现的次数
# str.find(sub) 查询sub这个字符串在str中是否存在，如果不存在结果为-1，如果存在，结果为sub首次出现的索引
# str.index(sub) 功能与find()相同，区别在于要查询的子串sub不存在时，程序报错
# str.stratswith(s) 查询字符串str是否以子串s开头
# str.endswith(s) 查询字符串str是否以子串s结尾

# 大小写转换
s1='HelloWorld'
new_s1=s1.lower()
print(s1,new_s1)
new_s2=s1.upper()
print(new_s2)

# 字符串的分割
e_mail='surwing@163.com'
lst=e_mail.split(sep='@')
print('邮箱名：', lst[0], '邮件服务器域名：', lst[1], sep='\t\t')

print(s1.count('o')) # 'o'在字符串s1中出现了两次

# 检索操作
print(s1.find('o')) # 查找'o'在字符串s1中首次出现的位置
print(s1.find('p')) # -1，没有找到
print(s1.index('o'))
# print(s1.index('p')) # ValueError: substring not found

# 判断前缀和后缀

print(s1.startswith('H')) # True
print(s1.startswith('P')) # False

print('demo.py'.endswith('.py')) # True # 判断文件类型（Python文件）
print('text.txt'.endswith('.txt')) # True

# str.replace(old,news) 使用news替换字符串str中所有的old字符串，结果是一个新的字符串
# str.center(width,fillchar) 字符串str在指定的宽度范围内居中，可以使用fillchar进行填充
# str.join(iter) 在iter中的每个元素的后面都添加一个新的字符串str
# str.strip(chars) 从字符串中去点左侧和右侧chars中列出的字符串
# str.lstrip(chars) 从字符串中去点左侧chars中列出的字符串
# str.rstrip(chars) 从字符串中去掉右侧chars中列出的字符串

s='HelloWorld'
# 字符串的替换
new_s=s.replace('o','HI')
print(new_s)
new_s1=s.replace('o','HI',count=1) # count指定替换次数，默认为全部替换
print(new_s1)

# 字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))

# 去掉字符串左右的空格
s='    Hello    World    '
print(s.strip())
print(s.lstrip()) # 去掉字符串左侧的空格
print(s.rstrip()) # 去掉字符串右侧的空格

# 去掉指定的字符
s3='dl-HelloWorld'
print(s3.strip('ld')) # -HelloWor # 与顺序无关
print(s3.lstrip('ld')) # -HelloWorld
print(s3.rstrip('ld')) # dl-HelloWor 
