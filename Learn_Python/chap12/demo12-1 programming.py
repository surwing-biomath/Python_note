# 什么是通信协议？
# 协议即规则，为了使全世界不同类型计算机可以连接起来，制定了一套全球通用的通信协议——Internet协议（IP）。
# 有了Internet协议，任何私有网络，只要支持这个协议，就可以接入互联网。

# 四层协议：
# 四层协议是一个分层的协议：应用层、传输层、网际层和网络接口层。
# 1. 应用层：应用层协议是直接为用户提供服务的协议，如HTTP、FTP、SMTP等。
# 2. 传输层：传输层协议负责在主机之间传输数据，如TCP、UDP等。
# 3. 网际层：网络层协议负责在网络中传输数据包，如IP协议。
# 4. 网络接口层：链路层协议负责在物理网络中传输数据帧，如Ethernet协议。

# TCP/IP协议:
# IP协议是整个TCP/IP协议族的核心协议
# IP地址就是互联网上计算机的唯一标识
# 目前的IP地址有两种表示方式：IPv4（十进制点分制）和IPv6（十六进制）
# 在命令行下使用ipconfig命令可以查看本机的IP地址

# TCP（Transmission Control Protocol）协议即传输控制协议，是建立在IP协议基础之上的。
# TCP协议负责两台计算机之间建立可靠连接，保证数据包按顺序发送到。
# 它是一种可靠的、一对一的、面向有连接的通信协议。

# UDP协议又被成为用户数据报协议（User Datagram Protocol），它是面向无连接的协议，
# 只要知道对方的IP地址和端口号，就可以直接发送数据包，由于是面向无连接的，所以无法保证数据一定会到达接收方。

# 端口号：
# 端口号是区分计算机中的运行的应用程序的整数
# 端口号的取值范围是0到65535，一共65536个端口号，
# 其中80这个端口号分配给了HTTP服务，21分配给了FTP服务，25分配给了SMTP服务，
# 110分配给了POP3服务，443分配给了HTTPS服务。

# TCP协议与UDP协议的区别：
# 1. TCP是面向连接的协议，而UDP是面向无连接的协议。
# 2. 安全方面：TCP协议传输消息可靠、不丢失、按顺序到达，UDP协议无法保证不丢包
# 3. 传输效率方面：TCP协议传输效率相对较低，UDP协议传输效率高
# 4. 连接对象数量方面：TCP协议只能是点对点、一对一的连接，UDP协议支持一对一、一对多、多对多的交互通信

# Socket对象的常用方法：
# 1. bind((ip, port)):      绑定ip地址和端口号
# 2. listen(N):             开始TCP监听，N表示操作系统挂起的最大连接数量，取值1~5之间，一般设置为5
# 3. accept():              被动接受TCP客户端连接，阻塞式
# 4. connect((ip, port)):   主动初始化TCP服务器连接，连接到指定ip地址和端口号的服务器
# 5. recv(size):            接受TCP数据，返回值为字符串类型，size表示要接受的最大数据量
# 6. send(str):             发送TCP数据，返回值是要发送的字节数量
# 7. sendall(str):          完整发送TCP数据，将str中的数据发送到连接的socket（套接字），返回之前尝试发送的所有数据，如果成功为None，失败抛出异常
# 8. recvfrom():            接受UDP数据，返回值为一个元组（data, address），data表示接收到的数据，address表示发送数据的套接字地址
# 9. sendto(data, (ip, port)): 发送UDP数据，返回值是发送的字节数
# 10. close():              关闭socket连接#

# TCP服务器端流程如下：
# 1. 使用socket类创建一个套接字对象
# 2. 使用bind(ip, port)方法绑定ip地址和端口号
# 3. 使用listen(N)方法开始TCP监听
# 4. 使用accept()方法等待客户端的连接
# 5. 使用recv()/send()方法接受/发送数据
# 6. 使用close()方法关闭套接字

from socket import socket, AF_INET, SOCK_STREAM
# AAF_INET用于Internet之间的进程通信
# SOCK_STREAM表示的用TCP协议编程

# （1）创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)
# （2）绑定ip地址和端口号
ip = '172.28.193.155'
port = 8888
server_socket.bind((ip, port))

# （3）使用listen()方法开始TCP监听
server_socket.listen(5)
print("服务器启动成功，等待客户端连接...")

# （4）使用accept()方法等待客户端的连接
client_socket, addr = server_socket.accept()  # 对元组进行系列解包复制

# （5）接受来自客户端的数据
data = client_socket.recv(1024)  # 接受1024字节的数据
print("接收到来自客户端的数据：", data.decode('utf-8'))  # 要求客户端发送过来的数据是使用utf-8编码的

# （6）关闭socket连接
server_socket.close()  # 关闭服务器连接
