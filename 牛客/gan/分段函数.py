import sys

n = int(sys.stdin.readline().strip())


def fen(num):
    if 0 <= num < 2:
        print("y=" + format(2.5 - num, '.1f'))
    elif 2 <= num < 4:
        print("y=" + format(2 - 1.5 * (num - 3) * (num - 3), '.1f'))
    elif 4 <= num < 6:
        print("y=" + format(num / 2 - 1.5, '.1f'))


for _ in range(n):
    m = int(sys.stdin.readline().strip())
    fen(m)
