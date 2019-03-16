# 首次出现的ID为主ID
import sys


if __name__ == "__main__":
    # 读取第一行的n
    while True:

        try:
            n = int(sys.stdin.readline().strip())
        except:
            break

        ip_info = dict()

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

        if n <= 0:
            break
        print('over')
