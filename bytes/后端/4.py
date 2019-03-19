import sys

n, m = sys.stdin.readline().strip().split(' ')

bb = sorted([int(x) for x in sys.stdin.readline().strip().split(' ')])
if m <= n:
    print(bb[n-m])
else:
    cha = m - n
    cc = bb[:]
    while cc:
        j = cc.pop()
        g = j/2
