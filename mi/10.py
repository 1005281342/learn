def climb_stairs(n):
    way = [0, 1, 2]
    for i in range(3, n + 1):
        way.append(way[i - 1] + way[i - 2])
    return way[n]


def easy_climb(n):
    return easy_climb(n - 1) + easy_climb(n - 2) if n not in [0, 1, 2] else n


# print(easy_climb(8))


def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n - 1) + f(n - 2)


import sys

d = [0, 1, 2]

N = 0


def dp(n):
    for _ in range(2, N-len(d)+3):
        d.append(d[-1] + d[-2])


for line in sys.stdin:
    line = int(line.strip())
    if N < line:
        N = line
        dp(line)
    print(d[line])

