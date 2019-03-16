# 首次出现的ID为主ID
import sys


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    if n <= 0:
        print('over')

    ip_info = dict()
    # print(n)
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    for _ in range(n):
        line = sys.stdin.readline().strip()
        name, ip = line.split(' ')
        if ip_info.get(ip):
            ip_info[ip].append(name)
        else:
            ip_info[ip] = [name]
    # print(ip_info)
    name_map = {a: b for a, b in ip_info.values()}

    for nk in sorted(name_map.keys()):
        print(name_map[nk], "is the MaJia of", nk)
    print('over')
