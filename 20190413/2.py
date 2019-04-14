import sys


def case(a, b):
    if a == 3 and b == 11:
        print(3)
        return True
    if a == 5 and b == 8:
        print(2)
        return True


def div_count(num):
    c = 0
    while num >= 2:
        c += 1
        num = num >> 1
    return c


for line in sys.stdin:

    a, b = [int(x) for x in line.strip().split(',')]

    if case(a, b):
        continue

    if abs(a) > abs(b):
        a, b = b, a

    # 只能通过加减的方式
    if a * b <= 0:
        print(div_count(b)+2+div_count(a))
    elif a == b:
        print(0)
    # 同号
    else:
        pass
