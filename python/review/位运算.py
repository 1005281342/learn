"""

    计算机中快速完成 乘除法

    前提是 x是整型
    左移 <<
        x << 1 相当于 x = x*2
    右移
        x >> 1 相当于 x = x//2
    直接操作二进制， 省内存， 效率高

"""

x = 5

x = x << 1
print(x)

x = x >> 2
print(x)


"""

    按位与 &
    按位或 |
    按位异或 ^
    按位取反 ~
"""
a = 5
b = 25
print("&", a & b)
print("|", a | b)
print("^", a ^ b)
print("~a", ~a)
