"""
    0。实例化客户端
    1。连接服务端
    2。向服务端发送信息
    3。接收服务端返回的信息
"""

import socket

# 实例化客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端
client.connect(('127.0.0.1', 6959))

while True:
    # 向服务端发起请求
    req_data = input()
    client.send(req_data.encode("utf8"))

    # 接收服务端返回的信息
    recv_data = client.recv(1024)
    print(recv_data.decode("utf8"))
