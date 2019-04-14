import sys


def min_distance(s1, s2):

    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))
    # 初始化
    dp = [[i + j for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            tmp_dist = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + tmp_dist)
    return dp[-1][-1]


while True:
    try:
        a = sys.stdin.readline().strip()
        b = sys.stdin.readline().strip()
        print(min_distance(s1=a, s2=b))
    except:
        break
