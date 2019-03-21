import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    m = int(sys.stdin.readline().strip())

    if m > 0:
        print(sum([x for x in range(m, m+m+1)]))
    else:
        print(sum([x for x in range(m+m, m+1)]))