import sys


def big_f(n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return (c ** d) * big_f(n - 1) * big_f(n - 2)


for line in sys.stdin:
    line = line.strip()

    a, b, c, d, mod, n = [int(h) for h in line.split(' ')]
    xi_l = [big_f(x) % mod for x in range(1, n + 1)]
    xi = 1
    for x in xi_l:
        xi *= x
    xi %= mod
    print((9 - len(str(xi))) * '0' + str(xi))
