def lcs(str1, str2):
    length_1 = len(str1)
    length_2 = len(str2)

    dp = [[0] * (length_2 + 1) for _ in range(length_1 + 1)]

    for i in range(1, length_1 + 1):

        for j in range(1, length_2 + 1):

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[length_1][length_2]


s = lcs('aceeefff', 'ggaccbdd')
print(s)
