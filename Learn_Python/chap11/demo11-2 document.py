# 文件的状态和操作过程
# |||（磁盘）存储状态 |||   --  (1)打开文件: file=open(......)  -->  ||| Python程序（内存）占用状态 |||  <----  （2）操作文件 (file.write(s), file.read())
#                         <--  (3)关闭文件：file.close()      ---

# 文件的打开模式：
# r: 以只读模式打开，文件指针在文件的开头，如果文件不存在，程序抛异常
# rb:以只读模式打开二进制文件，如图片文件
# w: 覆盖写模式，文件不存在创建，文件存在则内容覆盖
# wb:覆盖写模式写入二进制数据，文件不存在创建，文件存在则覆盖
# a: 追加写模式，文件不存在创建，文件存在，则在文件最后追加内容
# +: 与w/r/a等一同使用，在原功能的基础上增加同时读写功能

# 读写方法：
# file.read(size):      从文件中读取size个字符或字节，如果没有给定参数，则读取文件中的全部内容
# file.readline(size):  读取文件中的一行数据，如果给定参数，则为读取这一行中的size个字符或字节
# file.readlines():     从文件中读取所有内容，结果为列表类型
# file.write(s):        将字符串s写入文件
# file.writelines(lst): 将内容全部为字符串的列表lst写入文件
# file.seek(offset):    改变当前文件操作指针的位置，英文占一个字节，中文gbk编码占两个字节，utf-8编码占三个字节

def my_write(s):
    # 打开（创建）文件
    f = open('b.txt', 'a', encoding='utf-8')
    # 写入文件
    f.write(s)
    f.write('\n')
    # 关闭文件
    f.close()

def my_write_lst(file, lst):
    # 打开（创建）文件
    f = open(file, 'a', encoding='utf-8')
    # 操作文件
    f.writelines(lst)
    # 关闭文件
    f.close()

if __name__ == '__main__':
    # my_write('伟大的中国梦')
    # my_write('北京欢迎你')
    lst = ['姓名\t', '年龄\t', '成绩\n', '小明\t', '18\t', '99\n', '小红\t', '19\t', '98\n']
    my_write_lst('c.txt', lst)

