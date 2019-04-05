import math


def like_sqrt(num: int):
    xi = num / 2
    xt = xi
    xi = (xt + num / xt) / 2
    count = 1
    eps = 0.1 ** 6

    while abs(xi - xt) > eps:
        xt = xi
        xi = (xt + num / xt) / 2

        count += 1
    print(xi)


print(math.sqrt(3))
like_sqrt(3)