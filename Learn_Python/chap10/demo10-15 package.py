import jieba

# 读取文件内容
with open('华为笔记本.txt', 'r', encoding='utf-8') as file:
    s = file.read()
# print(s)

# 分词
lst = jieba.lcut(s)
# print(lst)
# 去重操作
set1 = set(lst)     # 使用集合实现去重

d = {}
for item in set1:
    if len(item) > 1:
        d[item] = lst.count(item)

new_lst = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 按照词频排序
print(new_lst)
