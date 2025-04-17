# 存储在计算机的存储设备中的一组数据序列就是文件
# 不同类型的文件通过后缀名进行区分
# 文本文件：由于编码格式的不同，所占磁盘空间的字节数不同
# 二进制文件：没有统一的编码，文件直接由0和1组成，需要使用指定的软件才能打开
# 例如：exe文件、doc文件、jpg文件等

# Python操作文件的步骤：
# 1，打开文件：变量名 = open(filename, mode, encoding)
# 2，操作文件：变量名.read()、变量名.write(s)
# 3，关闭文件：变量名.close()

def my_write():
    # (1)(创建)打开文件，mode表示打开文件的方式，w表示写入模式
    f = open('a.txt', 'w', encoding='utf-8')
    # (2)操作文件
    f.write('伟大的中国梦')
    # (3)关闭文件
    f.close()

def my_read():
    # (1)(创建)打开文件，mode表示打开文件的方式，r表示读取模式
    f = open('a.txt', 'r', encoding='utf-8')
    # (2)操作文件
    s = f.read()
    print(type(s), s)
    # (3)关闭文件
    f.close()

# 主程序运行
if __name__ == '__main__':
    # my_write()  # 调用函数
    my_read()  # 调用函数 