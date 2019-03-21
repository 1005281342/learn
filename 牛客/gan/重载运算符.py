import sys
from math import sin, pi

n = int(sys.stdin.readline().strip())
for _ in range(n):

    a, b = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    print(format(sin((a - b)/180*pi), '.2f'))
