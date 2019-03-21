import sys

m = int(sys.stdin.readline().strip())
for _ in range(m):
    _ = int(sys.stdin.readline().strip())
    v_list = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    x = int(sys.stdin.readline().strip())
    count = 0
    for i, v in enumerate(v_list):
        count += x**i*v
    print(count)
