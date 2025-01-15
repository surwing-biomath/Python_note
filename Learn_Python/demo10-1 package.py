# 模块：在Python中一个后缀名为.py的Python文件就是一个模块
# 模块中可以定义函数、类等
# 模块也可以避免函数、类、变量等名称相冲突的问题
# 模块不仅提高了代码的可维护性，同时还提高了代码的可重用性
# 在给模块命名的时候要求全部使用小写字母，多个单词之间使用下划线进行分割
# 如果自定义模块名称与系统内置模块名称相同，那么在导入时会优先导入自定义的模块

# 模块分为系统内置模块与自定义模块
# 系统内置模块：由开发人员编写好的模块，在安装Python解释器时一同安装到计算机
# 自定义模块：一个以.py结尾的文件就是一个模块，新建Python文件，实际上就是在新建模块
# 自定义模块的作用：规范代码，将功能相同的函数、类等封装到一个模块中，让代码更易于阅读
# 同时，可以被其他模块调用，提高开发效率

# 模块的导入：模块编写完成就可以被其他模块进行调用并使用被调用模块中的功能：
# import导入方式的语法结构：       import 模块名称 [as 别名]
# from...import导入方式的语法结构：from 模块名称 import 变量/函数/类/*

# (1) import  
import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name)
a.info()

# from...import
from my_info import name
print(name)

from my_info import info
info()

# 通配符
from my_info import *
print(name)
info()

# 同时导入多个模块
import math,time,random