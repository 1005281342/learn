import sys

n = sys.stdin.readline().strip()


def check(string: str):
    c = 10000
    while c > 0:
        # 检测三字母
        for i in range(len(string) - 2):
            try:
                if string[i] == string[i + 1] == string[i + 2]:
                    string = string.replace(string[i], '', 1)
                    i -= 1
            except:
                continue
        for i in range(len(string) - 3):
            try:
                if (string[i] == string[i+1]) and (string[i+2] == string[i+3]):
                    string = string.replace(string[i+3], '', 1)
                    # i += 1
                    i -= 1

            except:
                continue
        c -= 1
    print(string)


for _ in range(int(n)):
    # 读取每一行
    line = sys.stdin.readline().strip()
    check(line)
