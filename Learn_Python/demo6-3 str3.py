# 字符串的解码和编码
# 网络传输：str--(encoding)->bytes--(decoding)->str 
# 字符串的编码：将str类型转换成bytes类型，需要用到字符串的encode()方法
# 语法格式：str.encode(encoding= 'utf-8', errors= 'strict/ignore/replace')
# 字符串的解码：将bytes类型转换成str类型，需要用到字符串的decode()方法
# 语法格式：bytes.decode(encoding= 'utf-8', errors= 'strict/ignore/replace')

s='伟大的中国梦'
# 编码 str——>bytes
s_encode=s.encode(errors='replace') # 默认是utf-8，因为utf-8中文占3个字节
print(s_encode)
s_encode_gbk=s.encode('gbk',errors='replace') # gbk中中文占2个字节
print(s_encode_gbk)

# 编码中的出错问题
s2='耶✌'
# s_encode1=s2.encode('gbk','strict') # UnicodeEncodeError: 'gbk' codec can't encode character '\u270c' in position 1: illegal multibyte sequence
# print(s_encode1)
s_encode2=s2.encode('gbk','ignore')   # b'\xd2\xae'
print(s_encode2) 
s_encode3=s2.encode('gbk','replace')  # b'\xd2\xae?'
print(s_encode3)

# 解码过程bytes——>str
print(s_encode_gbk.decode('gbk'))       # 伟大的中国梦
print(bytes.decode(s_encode_gbk,'gbk')) # 伟大的中国梦
print(s_encode.decode())                # 伟大的中国梦

