import sys


def is_run(year) -> bool:
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False


r_d = {
    1: 31,
    3: 31,
    5: 31,
    7: 31,
    8: 31,
    10: 31,
    12: 31,

    4: 30,
    6: 30,
    9: 30,
    11: 30,
    # 31: {1, 3, 5, 7, 8, 10, 12},
    # 30: {4, 6, 9, 11}
}

n = int(sys.stdin.readline().strip())
for _ in range(n):
    y, m, d = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    i_r = is_run(y)
    if i_r:
        r_d[2] = 29
    else:
        r_d[2] = 28

    for i in range(1, m):
        d += r_d[i]

    print(d)
