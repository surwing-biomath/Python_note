# lst=['京A8888','津B6666','吉A7766']
# for item in lst:
#     area=item[0:1]
#     print(item,'归属地为：',area)


# s='HelloPython,HelloJava,Hellophp'
# word=input('请输入要统计的字符（不区分大小写）：')
# print('{0}在{1}中一共出现了{2}'.format(word,s,s.upper().count(word.upper())))


# lst=[
#     ['01','电风扇','美的',500],
#     ['02','洗衣机','TCL',1000],
#     ['03','微波炉','老板',400]
# ]
# print('编号\t\t机器\t\t品牌\t\t价格') # 使用两个\t会让输出更加美观
# for row in lst:
#     for col in row:
#         print(col,end='\t\t')
#     print()
# # 格式化字符串
# for row in lst:
#     row[0]='0000'+row[0]
#     row[3]='￥{0:.2f}'.format(row[3])

# print('编号\t\t机器\t\t品牌\t\t价格')
# for row in lst:
#     for col in row:
#         print(col,end='\t\t')
#     print()


