# 语法结构： print(输出内容)
# 完整语法格式：print(value, ..., sep='', end='\n', file=None)

a = 100
b = 50
print(90)
print(a) # 输出的是变量的值
print(a*b)

print('北京欢迎你1！')
print("北京欢迎你2！")
print('''北京欢迎你3！''')
print("""北京欢迎你4！""")

# 不换行一次输出多个数据
print(a, b, a*b, "北京欢迎你")

# 输出ASCII码对应的字符, 使用chr()将98转换成ASCII表中的字符
print("b", chr(98))
print("C", chr(67))
print(8, chr(56))
print("[", chr(91))

# 输出中文Unicode码
print(ord("北"), ord("京")) # ord()获取Unicode码
print(chr(21271), chr(20140))

# 将内容输出到文件
fp = open('note.txt', 'w') # open file, w-->write
print("北京欢迎你", file=fp)
fp.close() # close file

# 多条print函数输出一行显示
print('北京', '上海', sep=' a ', end='-->')
print('欢迎你') # 没有结束符， 所以会有空行

# 使用连接符连接多个字符串
print('北京欢迎你'+'2023')