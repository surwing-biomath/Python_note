# print('welcome to Beijing')
# name='louis'
# print(name)
# code in module_b.py is:
# # 导入的代码
# import module_a
# if we run module_b.py, the output is:
# welcome to Beijing
# louis

if __name__ == '__main__':
    print('welcome to Beijing')
    name='louis'
    print(name)
# 在导入到其他模块时，代码不希望被执行，将不希望执行的代码放入主程序代码中