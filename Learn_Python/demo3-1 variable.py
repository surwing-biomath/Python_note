# 保留字: Python中被赋予特定意义的一些单词，
# 不可以作为变量、函数、类、模块和其他对象的名称使用
# 保留字严格区分大小写
# ['False',  'None',   'True',    'and',      'as',       'assert', 'async',
#  'await',  'break',  'class',   'continue', 'def',      'del',    'elif',
#  'else',   'except', 'finally', 'for',      'from',     'global', 'if',
#  'import', 'in',     'is',      'lambda',   'nonlocal', 'not',    'or',
#  'pass',   'raise',  'return',  'try',      'while',     'with',  'yield']

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

# 标识符命名规则：
# 可以是字符（中文、英文）、下划线"_"、数字，并且第一个字符不能是数字
# 不能使用Python保留字
# 严格区分大小写
# 以下划线开头的标识符具有特殊意义，一般应避免使用相似的标识符
# 允许使用中文作为标识符，但不建议使用

# 标识符命名规范：
# 模块名尽量短小，并且全部使用小写字母，可以使用下划线分割多个字母。例如，grame_main
# 包名尽量短小，并且全部使用小写字母，不推荐使用下划线。例如，com.louispython，不推荐使用 com_louispython
# 类名采用单词首字母大写形式（Pascal风格）。例如，MyClass
# 模块内部的类采用"_" + Pascal 风格的类名组成。例如，在MyClass中的内部类 _InnerMyClass
# 函数、类的属性和方法的命名，全部使用小写字母，多个字母之间使用下划线分割
# 常量命名时全部采用大写字母，可以使用下划线
# 使用单下划线开头的模块变量或函数是受保护的，在使用 "from xxx import *" 语句从模块中导入时，这些模块变量或函数不能被导入
# 使用双下划线"__"开头的实例变量或方法是类私有的
# 以双下划线开头和结尾的是Python的专用标识符，例如：__init__() 表示初始化函数

# 变量名必须是一个有效标识符，不能使用保留符
# 变量谨慎使用i,O
# 常量在运行过程中值不可以修改
# 常量全部使用大写字母和下划线命名

luck_number = 8
name = 'Louis'
print('variable type is', type(luck_number))
print('the luck number of', name, 'is: ', luck_number)

# Python动态修改变量数据类型， 允许多个变量指向同一个值
no = number = 1024
print(no, number)
print(id(no)) # id()查看对象的内存地址
print(id(number))

pi = 3.1415926 #可以修改
PI = 3.1415926 # 不可以修改

