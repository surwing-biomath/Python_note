# 数据的验证：程序对用户输入的数据进行“合法”性验证
# str.isdigit()   所有字符都是数字（阿拉伯数字）
# str.isnumeric() 所有字符都是数字
# str.isalpha()   所有字符都是字母（包含中文字符）
# str.isalnum()   所有字符都是数字或字母（包含中文字符）
# str.islower()   所有字符都是小写
# str.isupper()   所有字符都是大写
# str.istitle()   所有字符都是首字母大写
# str.issapce()   所有字符都是空白字符（\n,\t等）

# isdigit() 十进制的阿拉伯数字
print('123'.isdigit())    # True
print('一二三'.isdigit())  # False
print('0b1010'.isdigit()) # False
print('ⅢⅢⅢ'.isdigit())  # False
print('-'*50)
# isnumeric() 数字
print('123'.isnumeric())    # True
print('一二三'.isnumeric())  # True
print('0b1010'.isnumeric()) # False
print('ⅢⅢⅢ'.isnumeric())  # True
print('壹贰叁'.isnumeric())  # True
print('-'*50)
# isalpha() 字母（包含中文字符）
print('hello你哈'.isalpha())      # True
print('hello你哈123'.isalpha())   # False
print('hello你哈一二三'.isalpha()) # True
print('hello你哈ⅢⅢⅢ'.isalpha()) # False
print('hello你哈壹贰叁'.isalpha()) # True
print('-'*50)
# 数字或字母
print('hello你哈'.isalnum())      # True
print('hello你哈123'.isalnum())   # True
print('hello你哈一二三'.isalnum()) # True
print('hello你哈ⅢⅢⅢ'.isalnum()) # True
print('hello你哈壹贰叁'.isalnum()) # True
print('-'*50)
# 判断字符的大小写
print('Helloworld'.islower())  # False
print('helloworld'.islower())  # True
print('hello你好'.islower())   # True
print('-'*50)
print('Helloworld'.isupper())  # False
print('HELLOWORLD'.isupper())  # True
print('HELLO你好'.isupper())   # True
print('-'*50)
# 所有字符都是首字母大写
print('Hello'.istitle())       # True
print('HelloWorld'.istitle())  # False
print('Helloworld'.istitle())  # True
print('Hello World'.istitle()) # True
print('Hello world'.istitle()) # False
print('-'*50)
# 判断是否都是空白字符
print('\t'.isspace()) # True
print('\n'.isspace()) # True
print(' '.isspace())  # True