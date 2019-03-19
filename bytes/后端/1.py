import sys

# 纸币之间存在倍数关系
n = sys.stdin.readline().strip()
b = 1024 - int(n)
c = 0
r_1 = b % 4 // 1
r_4 = (b % 16) // 4
r_16 = (b % 64) // 16
r_64 = b // 64

print(r_1, r_4, r_16, r_64)
c = r_1 + r_4 + r_16 + r_64

print(c)