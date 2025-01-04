# lst=[88, 89, 90, 98, 00, 99]
# print(lst) # [88, 89, 90, 98, 0, 99]

# for i in range(len(lst)):
#     if str(lst[i])!='0':
#         lst[i]=eval('19'+str(lst[i]))
#     else:
#         lst[i]=eval('200'+str(lst[i]))
# print(lst)

# for index, value in enumerate(lst):
#     if value!=0:
#         lst[index]=eval('19'+str(value))
#     else:
#         lst[index]=eval('200'+str(value))
# print(lst)

# # 创建空列表存储入库的商品信息
# lst=[]
# for i in range(5):
#     goods=input('请输入商品的编号和商品的名称进行商品入库,每次只能选择一件商品:')
#     lst.append(goods)
# # 输出所有商品信息
# for item in lst:
#     print(item)
# # 创建空列表用于存储购物车中的商品
# cart=[]
# while True:
#     flag=False # 代表没有商品的情况
#     num=input('请输入要购买的商品编号:')
#     # 遍历商品列表,查询要购买的商品是否存在
#     for item in lst:
#         if num==item[0:4]: # 从商品中切出序号
#             flag=True # 代表商品以找到
#             cart.append(item)
#             print('商品已成功添加到购物车')
#             break # 退出for循环
#     if not flag and num!='q':
#         print('商品不存在')
    
#     if num=='q':
#         break
# print('-'*50)
# print('您购物车里已选择的商品为:')
# cart.reverse()
# for item in cart:
#     print(item)

# 创建字典存储车票信息,使用车次做key,使用其他信息做value
# dict_ticket={
#     'G1569':['北京南-天津南', '18:06', '18:39', '00:33'],
#     'G1567':['北京南-天津南', '18:15', '18:49', '00:34'],
#     'G8917':['北京南-天津西', '18:20', '19:19', '00:59'],
#     'G203':['北京南-天津南', '18:35', '19:09', '00:34']
# }
# print('车次            出发站-到达站           出发时间        到达时间        历时时长')
# for key in dict_ticket.keys():
#     print(key, end='\t\t')
#     for item in dict_ticket.get(key):
#         print(item, end='\t\t')
#     print()
# train_no=input('请输入要购买的车次:')
# info=dict_ticket.get(train_no, '车次不存在')
# if info!='车次不存在':
#     person=input('请输入乘车人,如果是多位乘车人使用逗号分隔:')
#     s=info[0]+' '+info[1]+'开'
#     print('您已购买了'+train_no+' '+s+',请'+person+'尽快换取纸质车票')
# else:
#     print('对不起,选择的车次可能不存在')