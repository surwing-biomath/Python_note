# import random
# import os
# import os.path

# # 函数式编程
# def create_filename():
#     filename_lst = [];
#     lst = ['水果', '蔬菜', '肉类', '海鲜', '零食']
#     code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     for i in range(1, 3001):
#         filename = ''
#         # 拼接文件
#         if i < 10:
#             filename = '000' + str(i)
#         elif i < 100:
#             filename = '00' + str(i)
#         elif i < 1000:
#             filename = '0' + str(i)
#         else:
#             filename = str(i)
#         # 拼接类别
#         filename += '-' + random.choice(lst) + '-'
#         # 拼接识别码
#         s = ''
#         for j in range(9):
#             s += random.choice(code)
#         filename += s
#         filename_lst.append(filename)
#     return filename_lst

# # 创建文件的函数
# def create_file(filename):
#     # 创建文件
#     with open(filename, 'w') as f:
#         pass


# if __name__ == '__main__':
#     # 在指定的路径下创建文件
#     path = './chap11/date'
#     if not os.path.exists(path):
#         os.makedirs(path)

#     lst = create_filename()
#     # 创建文件
#     for filename in lst:
#         create_file(os.path.join(path, filename) + '.txt')
    
#     # print(create_filename())

# import os
# import os.path

# # 函数式编程
# def mkdirs(path, num):
#     for item in range(1, num + 1):
#         os.mkdir(path + '/' + str(item))

# if __name__ == '__main__':
#     # 在指定的路径下创建文件
#     path = './chap11/newdir'
#     if not os.path.exists(path):
#         os.makedirs(path)

#     num = eval(input('请输入要创建的目录数量：'))
#     mkdirs(path, num)

# import time
# def show_info():
#     print('输入提示数字，执行相应的操作： 0.退出   1.查看登录日志')

# # 记录日志
# def write_loginfo(username):
#     with open('log.txt', 'a', encoding = 'utf-8') as file:
#         s = f'用户名{username}，登录时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}'
#         file.write(s)
#         file.write('\n')

# # 读取日志
# def read_loginfo():
#     with open('log.txt', 'r', encoding = 'utf-8') as file:
#         while True:
#             line = file.readline()
#             if line == '':
#                 break
#             else:
#                 print(line)


# if __name__ == '__main__':
#     # 记录登录日志
#     username = input('请输入用户名：')
#     pwd = input('请输入密码：')
#     if username == 'admin' and pwd == 'admin':
#         print('登录成功')
#         write_loginfo(username)
#         show_info()
#         num = eval(input('请输入提示数字:'))
#         while True:
#             if num == 0:
#                 print('推出成功')
#                 break
#             elif num == 1:
#                 print('查看登录日志:')
#                 read_loginfo()
#                 show_info()
#             else:
#                 print('输入错误，请重新输入')
#                 show_info()
#             num = eval(input('请输入提示数字：'))
#     else:
#         print('用户名或密码错误')


#     # write_loginfo(username)

def find_answer(question):
    with open('replay.txt', 'r', encoding = 'utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
        question = input('请输入问题：')
        while True:
            if 'bye' in question:
                break
            elif 'exit' in question:
                break
            elif 'quit' in question:
                break
            elif '再见' in question:
                break
            else:
                reply = find_answer(question)
                if reply == False:
                    question = input('我不知道你在说什么，您可以问我关于订单、物流、退款、投诉、评价、发货、收货、取消、支付等方面的问题，退出请输入bye：')
                else:
                    print(reply)
                    question = input('请继续提问，您可以问我关于订单、物流、退款、投诉、评价、发货、收货、取消、支付等方面的问题，退出请输入bye：')
        print('感谢您的使用，期待下次再见！')