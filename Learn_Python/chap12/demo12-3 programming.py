# 多次通信

# from socket import socket, AF_INET, SOCK_STREAM
import socket

# （1）创建socket对象
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# （2）绑定ip地址和端口号
ip = '172.28.193.155'
port = 8888
socket_obj.bind((ip, port))

# （3）使用listen()方法开始TCP监听
socket_obj.listen(5)

# （4）使用accept()方法等待客户端的连接
client_socket, addr = socket_obj.accept()  

# （5）接受来自客户端的数据
info = client_socket.recv(1024).decode('utf-8')         # while循环的四个步骤， info是初始化变量
while info != 'bye':                                # 条件判断
    if info != '':
        print('接收到来自客户端的数据：', info)
    # 准备发送的数据
    data = input('请输入要发送给客户端的数据：')

    # 服务器端回复客户端
    socket_obj.send(data.encode('utf-8'))
    if data == 'bye':
        break   # 退出循环                          # 循环体
    info = socket_obj.recv(1024).decode('utf-8')    # 改变变量

# （6）关闭socket对象
client_socket.close()
socket_obj.close()