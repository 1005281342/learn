import sys
from math import sqrt

n = int(sys.stdin.readline().strip())
for _ in range(n):

    a, b, c = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    if a == 0:
        try:
            print('x=' + format(-c / b, '.2f'))
        except:
            print(-1)
    else:
        dd = b * b - 4 * a * c
        if dd > 0:
            x1 = format((-b - sqrt(dd)) / 2 / a, '.2f')
            x2 = format((-b + sqrt(dd)) / 2 / a, '.2f')
            print("x1=" + x1 + ',' + "x2=" + x2)
        elif dd == 0:
            print("x=" + format(-b / 2 / a, '.2f'))

        else:
            print(-1)
