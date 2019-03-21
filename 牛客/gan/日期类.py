import sys

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

    2: 28
}

hh = int(sys.stdin.readline().strip())


def gui(string: str) -> str:
    string = str(string)
    if len(string) < 2:
        string = '0' + string
    return string


def add(num_list: str):
    y, m, d = num_list
    d += 1
    if d > r_d[m]:
        d = 1
        m += 1
    if m > 12:
        m = 1
        y += 1

    print('-'.join([gui(y), gui(m), gui(d)]))


for _ in range(hh):
    nums = [int(c) for c in sys.stdin.readline().strip().split(' ')]
    add(nums)
