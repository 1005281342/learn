import sys

m = int(sys.stdin.readline().strip())

for _ in range(m):
    res = ''
    for i, v in enumerate(list(sys.stdin.readline().strip())):
        if v in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            res += str(i + 1) + ' '
    print(res.strip())
