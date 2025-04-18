# os.path模块：是os模块的子模块，也提供了一些目录或文件的操作函数
# 函数名称             # 描述说明
# abspath(path)       # 获取目录或文件的绝对路径
# exists(path)        # 判断目录或文件在磁盘上是否存在，结果为bool类型，如果目录或文件在磁盘上存在，结果为True，否则为False
# join(path, name)    # 将目录与目录名或文件名进行拼接，相当于字符串的“+”操作
# splitext(path)      # 分别获取文件名和后缀名
# basename(path)      # 从path中提取文件名
# dirname(path)       # 从path中提取路径（不包含文件名）
# isdir(path)         # 判断path是否是有效路径
# isfile(path)        # 判断file是否是有效文件

import os.path
print('获取目录或文件的绝对路径：', os.path.abspath('./b.txt'))
print('判断目录或文件在磁盘上是否存在：', os.path.exists('b.txt'))  # 相对路径 True
print('判断目录或文件在磁盘上是否存在：', os.path.exists('newb.txt'))  # False
print('判断目录或文件在磁盘上是否存在：', os.path.exists('chap11'))  # True
print('拼接路径：', os.path.join('C:/Users/lenovo/OneDrive/Python_note/Learn_Python/chap11','b.txt'))
print('分割文件名和文件后缀名：', os.path.splitext('b.txt'))    # 元组类型 ('b', '.txt')
print('提取文件名：', os.path.basename('C:/Users/lenovo/OneDrive/Python_note/Learn_Python/chap11/b.txt'))  # 不包含路径 b.txt 
print('提取路径：', os.path.dirname('C:/Users/lenovo/OneDrive/Python_note/Learn_Python/chap11/b.txt'))  # 不包含文件名 C:/Users/lenovo/OneDrive/Python_note/Learn_Python/chap11

print('判断一个路径是否是有效路径：', os.path.isdir('C:/Users/lenovo/OneDrive - City University of Hong Kong - Student/Python_note/Learn_Python/chap11'))  # True
print('判断一个路径是否是有效路径：', os.path.isdir('C:/Users/lenovo/OneDrive - City University of Hong Kong - Student/Python_note/Learn_Python/chap110'))  # False
print('判断一个路径是否是有效文件：', os.path.isfile('C:/Users/lenovo/OneDrive - City University of Hong Kong - Student/Python_note/Learn_Python/chap11/b.txt'))  # True
print('判断一个路径是否是有效文件：', os.path.isfile('C:/Users/lenovo/OneDrive - City University of Hong Kong - Student/Python_note/Learn_Python/chap11/bbbbb.txt'))  # False