# 整数类型为没有小数部分的数值
# 十进制没有引导符，二进制为0b或0B，八进制为0o或0O，十六进制为0x或0X

num0 = 987
num1 = 0b10101
num2 = 0o07632
num3 = 0x87fab
print(num0, num1, num2, num3)

# 浮点数表示带有小数点的数值，复数单位为j，实部用 .real，虚部用 .imag

height0 = 181
height1 = 181.0
height2 = 1.8e2
print(height0, type(height0), height1, type(height1), height2, type(height2))
print(0.1+0.2) # 不确定的尾数问题 0.30000000000000004
print(round(0.1+0.2, 1)) # 保留一位小数
x = 1+2j
print(x.real, x.imag)

# 字符串类型为连续字符序列，可以表示计算机所能识别的一切字符，字符串的界定符分为单引号、双引号、三引号
# 转义字符：\n 换行符；\t 水平制表符，用于横向跳到下一个制表位；\" 双引号；\' 单引号；\\ 反斜杠
# 原字符：使转义字符失效的字符，r或R

city = 'HK'
address = "CityUHK"
print(city, address)

# 多行字符串
info0 = '''
city0: HK
address0: CityUHK
'''
info1 = """
city1: HK
address1 = CityUHK
"""
print('info0 is', info0, 'info1 is ', info1)

# 转义字符，原字符
print('beijing')
print('welcome')
print('------')
print('beijing\nwelcome')
print('bei\njing\nwel\ncome')
print(r'bei\njing\nwel\ncome')
print(R'bei\njing\nwel\ncome')
print('北京\t欢迎你') # \t
print('hello\toooo') # 一个制表位8个字符，hello五个字符，所以填充3个空格
print('hellooooo')
print('\'good good study\'', '\"day day up\"')

# 对字符串中某个字符的检索为索引，正向索引为从 0 到 n-1，反向索引为从 -1 到 -n
# 对字符串某个子串或区间的检索为切片，切片的语法结构：字符串或字符串变量[N:M]
s = 'helloworld'
print(s[0], s[-10])
print(s[0:5], s[-6:-1])
print(s[:5], s[5:])
print('北京欢迎你'[4])

# 字符串操作：x+y 拼接；x*n或n*x 复制n次；x in s 判断x是否为s子串
print('xy'*3, 3*'xy', 'xy' in 'abxyscx')

# bool type, True表示整数1，False表示整数0
# False或None
# 数值中的0，包含0，0.0, 虚数0
# 空序列， 包含空字符串、空元组、空列表、空字典、空集合
# 自定义对象的示例，该对象的 __bool__() 方法返回False或 __len__() 方法返回0
x = True
print(x, type(x), x+10, False+10)
print(bool(18), bool(0), bool(0.0), bool(0.2))
print(bool('beijing'), bool(''))
print(bool(True), bool(False), bool(None))

# 数据类型之间的转换
# int(),（只保留整数部分） float(), str(), chr(), ord(),（整数2字符、字符2整数 unicode） hex(),（整数2字符串） oct(), bin()

# eval函数，去掉字符串最外侧的引号，并按照Python语句方式执行去掉引号后的字符串，经常搭配input使用，获取输入的数值
s = '3.14+3'
print(s, type(s), eval(s), type(eval(s)))

age = eval(input('input age:')) # 字符串2int，相当于 int(age)

# 算术运算符：+, -, *, /, //, %, **
# 赋值运算符：=, +=, -=, *=, /=, //=, %=, **=
# 比较运算符：>, <, ==, !=, >=, <=
# 逻辑运算符：and, or, not
# 位运算   ：&, |, ^, ~, <<
# 优先级：（）---> ** ---> ~, +, - (positive, negative sign) ---> *, /, %, // ---> +, -
# ---> <<, >> ---> & ---> ^ ---> | ---> <, <=, >, >=, !=, == ---> =


