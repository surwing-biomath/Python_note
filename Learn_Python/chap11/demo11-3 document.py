def my_read(filename):
    # 打开
    file = open(filename, 'w+', encoding='utf-8')
    # 操作
    file.write('你好啊')    # 写入完成，文件的指针在最后
    # seek修改文件指针的位置
    file.seek(0)          # 将文件指针移动到开头
    # 读取
    # s = file.read()         # 读取文件中的所有内容
    # s = file.read(2)        # 你好，你好是两个字符
    # s = file.readline()     # 读取一行数据
    # s = file.readline(2)    # 读取一行中的两个字符
    # s = file.readlines()    # 读取所有行，返回一个列表，每行都为列表中的一个元素 # <class 'list'> ['你好啊']
    # 读取“好啊”
    file.seek(3)            # 三个字节，utf-8编码中，一个中文占三个字节
    s = file.read()         # 读取全部   <class 'str'> 好啊
    print(type(s), s)

    # 关闭
    file.close()

if __name__ == '__main__':
    my_read('d.txt')

