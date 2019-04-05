def func(x):
    return 2.0 * x * x + 3.2 * x - 1.8


def dichotomy_equation(a, b, f):
    esp = 0.1 ** 6
    mid = (a + b) / 2
    while abs(b - a) > esp:

        # 说明零点[方程解]存在于（a, mid）
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        mid = (a + b) / 2
    return mid


# 求 2.0 * x * x + 3.2 * x - 1.8 在 (-1,2)上的解
res = dichotomy_equation(-1, 2, func)
# 0.4409674406051636
print(res)
