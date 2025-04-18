# json模块的常用函数
# json.dumps(obj)       # 将Python数据类型转成JSON格式过程，编码过程
# json.loads(s)         # 将JSON格式字符串转成Python数据类型，解码过程
# json.dump(obj, file)  # 与dumps()功能相同，将转换结果存储到文件file中
# json.load(file)       # 与loads()功能相同，从文件file中读入数据

import json
# 准备高维数据
lst = [
    {'name':'张三', 'age':18,'score':90},
    {'name':'李四', 'age':19,'score':80},
    {'name':'王五', 'age':20,'score':70},
    {'name':'陈六', 'age':21,'score':60}
]

s = json.dumps(lst, ensure_ascii=False, indent=4)  # ensure_ascii=False表示中文不转义,防止中文乱码，正常显示中文，indent=4表示缩进4个空格
print(type(s))   # <class 'str'> 编码，list---->str, 列表中是字典
print(s)

# 解码
lst2 = json.loads(s)  # 将JSON格式字符串转成Python数据类型，解码过程
print(type(lst2))  # <class 'list'> 解码，str---->list, 列表中是字典
print(lst2)  # [{'name': '张三', 'age': 18, 'score': 90}, {'name': '李四', 'age': 19, 'score': 80}, {'name': '王五', 'age': 20, 'score': 70}, {'name': '陈六', 'age': 21, 'score': 60}]

# 编码到文件中
with open('student.txt', 'w', encoding='utf-8') as file:
    json.dump(lst, file, ensure_ascii=False, indent=4)  # 将Python数据类型转成JSON格式过程，编码过程，存储到文件中

# 解码到程序
with open('student.txt', 'r', encoding='utf-8') as file:
    lst3 = json.load(file)  # 将JSON格式字符串转成Python数据类型，解码过程
    print(type(lst3))  # <class 'list'>
    print(lst3)  # [{'name': '张三', 'age': 18, 'score': 90}, {'name': '李四', 'age': 19, 'score': 80}, {'name': '王五', 'age': 20, 'score': 70}, {'name': '陈六', 'age': 21, 'score': 60}]

