# TCP客户端流程如下：
# 1. 使用socket类创建一个套接字对象
# 2. 使用connect((host, port))设置连接的主机IP和主机设置的端口号
# 3. 使用send()/recv()方法发送/接受数据
# 4. 使用close()方法关闭套接字

# 先去启动服务器端，再去启动客户端
# 因为服务器端处于监听状态，时刻在等待着客户端发送请求
# 如果没有启动服务器端，客户端就无法连接到服务器端

import socket
# （1）创建SOcket对象
client_socket = socket.socket()

# （2）IP地址和主机端口，向服务器端发送连接请求
ip = '172.28.193.155'
port = 8888
client_socket.connect((ip, port))
print('--------与服务器连接建立成功--------')

# （3）发送数据
client_socket.send('Welcome to Python world!'.encode('utf-8'))

#（4）关闭
client_socket.close()
print('--------发送完毕--------')