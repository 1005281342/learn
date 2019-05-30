import psutil
import socket
import uuid


def mac_name_ip():
    """ 获得Mac地址、计算机名、IP地址 """
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]  # Mac地址
    name = socket.getfqdn(socket.gethostname())  # 计算机名称
    addr = socket.gethostbyname(name)  # IP地址
    return mac, name, addr


def net_all():
    """ 获取网络总的IO信息 """
    n = psutil.net_io_counters()
    ns = [
        n.bytes_sent,  # 发送字节数
        n.bytes_recv,  # 接受字节数
        n.packets_sent,  # 发送数据包数
        n.packets_recv,  # 接收数据包数
    ]
    return ns


def net_line():
    """ 获取每个网络接口的IO信息 """
    n = psutil.net_io_counters(pernic=True)
    ns = {}
    for i in n:
        ns[i] = [
            n[i].bytes_sent,  # 发送字节数
            n[i].bytes_recv,  # 接受字节数
            n[i].packets_sent,  # 发送数据包数
            n[i].packets_recv,  # 接收数据包数
        ]
    return ns


def net_card():
    """ 网卡信息
        返回：{网卡名：[IP地址64，IP地址32，Mac地址]，...}
    """
    n = psutil.net_if_addrs()
    ns = {}
    for i in n:
        ns[i] = []
        for j in n[i]:
            ns[i].append(j.address)
    return ns


def net_cart_status():
    """ 网卡状态 """
    n = psutil.net_if_stats()
    return n


def network_connect():
    """ 网路连接信息 """
    n = psutil.net_connections()
    return n


if __name__ == '__main__':
    res = mac_name_ip()
    print(res)
