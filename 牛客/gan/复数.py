import sys

m = int(sys.stdin.readline().strip())

for _ in range(m):
    a, b, c, d = sys.stdin.readline().strip().split(' ')
    x = int(a) + int(c)
    y = int(b) + int(d)
    s = ''
    if x < 0:
        s += str(-x)
    else:
        s += str(x)

    if y < 0:
        s += str(-y) + 'i'
    else:
        s += str('+') + str(y) + 'i'

    print(s)
