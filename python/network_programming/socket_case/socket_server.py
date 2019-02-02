"""
    0。 实例化服务端，绑定窗口，监听[监听是一个阻塞的过程]
    1。 创建连接
    2。 接收客户端发送过来的信息
    3。 向客户端发送信息
    注意，socket通信传输的信息是字节码，并且双方都可以关闭通信
"""

import socket
import threading

# 实例化服务端
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定
server.bind(('0.0.0.0', 6959))

# 监听
server.listen(5)


def handle_sock(sock):
    while True:
        # 接收来自客户端的数据
        recv_data = sock.recv(1024)  # bufsize 指定数据流大小为1024字节
        print(recv_data.decode("utf8"))

        # 回复信息给客户端
        res_data = input()
        sock.send(res_data.encode("utf8"))


while True:
    # 接收客户端连接请求，并建立连接
    sock, __ = server.accept()

    # 用线程去处理新接收的连接(用户)
    client_thread = threading.Thread(target=handle_sock, args=(sock,))
    client_thread.start()
