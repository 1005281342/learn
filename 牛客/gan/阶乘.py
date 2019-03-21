import sys

n = int(sys.stdin.readline().strip())


def jie_c(x):
    if x <= 1:
        return 1
    else:
        return jie_c(x-1)*x


for _ in range(n):
    m = int(sys.stdin.readline().strip())

    print(jie_c(m))