# Python中的包：含有__init__.py文件的文件夹（目录）
# 可以避免模块名称相冲突的问题
# 主程序运行：
# if __name__== '__main__':
#     pass

import admin.my_admin as a              # 包名.模块名 admin是包名，my_admin是模块名，__init__.py文件会自动执行一次而且仅执行一次
a.info()                                # copyright louis
                                        # phd student
                                        # hello everyone, my names louis, and my age is 18
print('-'*50)

from admin import my_admin as b         # from 包名 import 模块名 as 别名
b.info()                                # hello everyone, my names louis, and my age is 18
print('-'*50)

from admin.my_admin import info         # from 包名.模块名 import 函数/变量等
info()                                  # hello everyone, my names louis, and my age is 18
print('-'*50)

from admin.my_admin import *            # from 包名.模块名 import *
print(name)                             # louis
print('-'*50)

