import sys
import math


def maximal_rectangle(matrix):
    if not matrix:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    dp = [[0] * columns for i in range(rows)]
    dp[0][0] = int(matrix[0][0])

    for i in range(1, columns):
        if matrix[0][i] == '1':
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    for i in range(1, rows):
        if matrix[i][0] == '1':
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = 0

    for i in range(1, columns):
        for j in range(1, rows):
            if matrix[j][i] == '0':
                dp[j][i] = 0
            else:
                dp[j][i] = dp[j - 1][i] + 1
    max_num = 0
    for i in range(rows):
        if max_num < choose_max(dp[i]):
            max_num = choose_max(dp[i])
    return max_num


def choose_max(nums):
    max_num = 0
    for i in set(nums):
        count = 0
        for j in nums:
            if j >= i:
                count += 1
                if max_num < count * i:
                    max_num = count * i
            else:
                count = 0
    return max_num


for line in sys.stdin:
    a = line.replace('\n', '').split(',')
    b = [[char for char in string] for string in a]
    # print(b)
    t_res = maximal_rectangle(b)
    res = int(math.sqrt(t_res)) ** 2
    print(res)
