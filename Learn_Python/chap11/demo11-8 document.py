# 目录和文件的相关操作
# OS: Python内置的与操作系统文件相关的模块，该模块中语句的执行结果
# 通常和操作系统有关，即有些函数的运行效果在Windows操作系统和MacOS系统中不一样。
# 函数名称           说明
# getcwd()          获取当前的工作路径
# listdir(path)     获取path路径下的文件和目录信息，如果没有指定path，则获取当前路径下的文件和目录信息
# mkdir(path)       在指定路径下创建目录（文件夹）
# makedirs(path)    创建多级目录
# rmdir(path)       删除path下的空目录
# removedirs(path)  删除多级目录
# chdir(path)       把path设置为当前目录
# walk(path)        遍历目录树，结果为元组，包含所有路径名、所有目录列表和文件列表
# remove(path)      删除path指定的文件
# rename(old, new)  将old重命名为new
# stat(path)        获取path指定的文件信息
# startfile(path)   启动path指定的文件，类似于双击打开文件

import os
print('当前工作路径:', os.getcwd())  # 获取当前的工作路径
lst = os.listdir()
print('当前路径下的文件和目录信息:', lst)  # 获取当前路径下的文件和目录信息
print('指定路径下所有目录即文件', os.listdir('./chap11'))
# 创建目录
# os.mkdir('testdir2') # 在当前路径下创建目录testdir  # 如果要创建的文件夹存在程序报错 # FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'testdir'
# os.makedirs('./testdir/testdir1/testdir2')
# 删除目录
# os.rmdir('./testdir2')       # 删除空目录testdir2  # 如果要删除的文件夹不存在程序报错 # FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'testdir2'
# os.removedirs('./testdir/testdir1/testdir2')  # 删除多级目录testdir/testdir1/testdir2
# 改变当前的工作路径
os.chdir('./chap11') # 把当前工作路径改为chap11
print('当前工作路径:', os.getcwd())  # 获取当前的工作路径

# 遍历目录树，结果为元组，包含所有路径名、所有目录列表和文件列表，相当于递归操作
for dirpath, dirnames, filenames in os.walk('../'):     # ../相当于回退到上级目录
    print('当前路径名:', dirpath)  # 当前路径名
    print('当前目录列表:', dirnames)  # 当前目录列表
    print('当前文件列表:', filenames)  # 当前文件列表
    print('-------------------------------------')

# 删除文件
# os.remove('./a.txt') # 删除文件a.txt, 如果要删除的文件不存在程序报错 # FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'a.txt'
# 重命名文件
# os.rename('./aa.txt', './newaa.txt')

# 转换时间格式
import time
def date_format(longtime):
    s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))
    return s

# 获取文件信息
info = os.stat('./newaa.txt')

print(type(info))  # <class 'os.stat_result'>
print(info)        # os.stat_result(st_mode=33206, st_ino=123004564822561147, st_dev=13025615267701970160, st_nlink=1, st_uid=0, st_gid=0, st_size=11, st_atime=1744949376, st_mtime=1744943286, st_ctime=1744943286)

print('最近一次访问时间：', date_format(info.st_atime)) 
print('在Windows操作系统中显示的文件创建时间：', date_format(info.st_ctime))
print('最后一次修改时间：', date_format(info.st_mtime))
print('文件大小：', info.st_size, '字节')  # 文件大小： 11 字节

# 启动路径下的文件
# os.startfile('calc.exe')  # 启动路径下的文件，类似于双击打开文件
# 启动Python解释器
os.startfile(r'C:\Users\lenovo\AppData\Local\Programs\Python\Python313\python.exe')  # '\'是Python中的转义字符，r''表示原始字符串，r''中的'\'不会被转义


