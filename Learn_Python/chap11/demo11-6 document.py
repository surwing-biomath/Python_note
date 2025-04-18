# 数据的组织维度及存储
# 数据的组织维度：也成为数据的组织方式或存储方式，在Python中常用的数据组织方式
# 可分为一维数据、二维数据和高维数据。
# 一维数据：通常采用线性方式组织数据，一般使用Python中的列表、元组或者集合进行存储数据
# 二维数据：也称表格数据，由行和列组成，类似于Excel表格，在Python中使用二维列表进行存储
# 高维数据：高维数据则是使用Key-Value对的方式进行组织数据，在Python中使用字典进行储存数据。
#          在Python中内置的json模块专门用于处理JSON(JavaScript Object Notation)格式的数据，JSON格式的数据就是一种高维数据的组织方式。

# 一维数据和二维数据的存储
def my_write():
    # 一维数据，可以使用列表、元组、或集合
    lst = ['张三', '李四', '王五','陈六']
    with open('student.csv', 'w', encoding='utf-8') as file:
        file.write(','.join(lst))      # 将列表转成字符串

def my_read():
    with open('student.csv', 'r', encoding='utf-8') as file:
        s = file.read()
        lst = s.split(',')           # 将字符串转成列表
        print(lst)

# 存储和读取二维数据
def my_write_table():

    lst = [
        ['商品名称', '单价', '数量'],
        ['苹果', '5.5', '3'],
        ['香蕉', '2.5', '5'],
        ['橙子', '4.0', '2']
    ]
    with open('table.csv', 'w', encoding='utf-8') as file:
        for item in lst:    # item的数据类型是列表
            line = ','.join(item)
            file.write(line)
            file.write('\n')
            
def my_read_table():
    data = []               # 存储读取的数据
    with open('table.csv', 'r', encoding='utf-8') as file:
        lst  = file.readlines() # 每一行是列表中的一个元素
        # print(type(lst), lst) # <class 'list'> ['商品名称,单价,数量\n', '苹果,5.5,3\n', '香蕉,2.5,5\n', '橙子,4.0,2\n']
        for item in lst:
            new_lst = item[:len(item) - 1].split(',')     # 结果是列表
            data.append(new_lst)
        print(data)          # [['商品名称', '单价', '数量'], ['苹果', '5.5', '3'], ['香蕉', '2.5', '5'], ['橙子', '4.0', '2']]

if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()