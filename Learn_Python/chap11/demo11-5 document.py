# with语句：又称上下文管理器，在处理文件时，无论是否产生异常，
# 都能保证with语句执行完毕之后关闭已经打开的文件，这个过程是自动的，无需手动操作
# 语法结构：
# with open(filename, mode) as file:
#     pass

def write_fun():
    with open('aa.txt', 'w', encoding='utf-8') as file:
        file.write('hello world')

def read_fun():
    with open('aa.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

def copy_fun(src_file, target_file):
    with open(src_file, 'r', encoding='') as src:
        with open(target_file, 'wb') as target:
            target.write(src.read())