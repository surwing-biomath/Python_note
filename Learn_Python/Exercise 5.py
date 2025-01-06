# try:
#     score=eval(input('请输入分数：'))
#     if 0<=score<=100:
#         print('分数为：',score)
#     else:
#         raise Exception('分数不正确')
# except Exception as e:
#     print(e)

# try:
#     a=eval(input('请输入第一条边长：'))
#     b=eval(input('请输入第二条边长：'))
#     c=eval(input('请输入第三条边长：'))
#     if a+b>c and b+c>a and c+a>b:
#         print(f'三角形边长为:{a},{b},{c}')
#     else:
#         raise Exception(f'{a},{b},{c}不能构成三角形')
# except Exception as e:
#     print(e)