import sys


def give(line):
    a = [int(x) for x in line.split(' ')]
    n = len(a)
    ans = {}
    bak = [0] * n
    for idx, _ in enumerate(a):

        ans[idx] = 1
        if 0 < idx < n - 1:
            if a[idx] > a[idx-1]:
                ans[idx] = ans[idx-1] + 1
            elif a[idx] > a[idx+1]:
                bak[idx] = -1
        elif idx == n-1:
            if a[idx] > a[idx-1]:
                ans[idx] = ans[idx-1] + 1
            elif a[idx] > a[0]:
                ans[idx] = ans[0] + 1

    for i, v in enumerate(bak):
        if v < 0:
            ans[i] = ans[i+1] + 1

    # print(ans)
    print(sum(ans.values()))


n_c = int(sys.stdin.readline().strip())

for _ in range(n_c):
    _ = int(sys.stdin.readline().strip())
    give(sys.stdin.readline().strip())
