"""
题目描述
N 个人围成一圈顺序编号，从1 号开始按1、2、3 顺序报数，报3 者退出圈外，
其余的人再从1、2、3 开始报数，报3 的人再退出圈外，依次类推。
请按退出顺序输出每个退出人的原序号。要求使用环行链表编程。

input
    1
    4

out
    3 2 4 1
"""

import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    m = int(sys.stdin.readline().strip())
    nums = [x for x in range(1, m+1)]
    # print(nums)
    count = 0
    tmp = []
    d = [0] * 3
    while len(tmp) < len(nums):
        # count = 0
        # d = deque(maxlen=3)
        for x in nums:
            if str(x) in tmp:
                continue
            d[count] = x
            # print(d[count], count)
            count += 1
            # print(d[-1])
            if d[2]:
                tmp.append(str(d[2]))
                count = 0
                d = [0] * 3

    print(' '.join(tmp))
