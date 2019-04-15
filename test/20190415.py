def format_el_room_type_id(el_id):
    el_id = str(int(el_id))

    return max(4 - len(el_id), 0) * '0' + el_id


# print(format_el_room_type_id('01'))
# print(format_el_room_type_id('0100'))
# print(format_el_room_type_id('000100'))

A = [0, 60, 80, 105, 115, 130, 150]
B = [0, 65, 85, 110, 140, 160, 175]
C = [0, 75, 100, 120, 135, 150, 180]
length = len(A)


# 找到最大的数的下标
def max_info(nums):
    a, b = -1, 0
    for i, v in enumerate(nums):
        if v > b:
            b = v
            a = i
    return a, b


def investment_problem():
    am = length * [0]
    bm = length * [0]
    cm = length * [0]
    # 贪心法, 从价值密度上看
    for i in range(1, length):
        am[i] = A[i] / i
        bm[i] = B[i] / i
        cm[i] = C[i] / i
    # abc = [am, bm, cm]
    # for j in range(1, length):
    #     x, y = max_info([am[j], bm[j], cm[j]])


# 最优解 1，4，1
def investment(n, m):
    # 初始化，在只有一个项目的情况下
    for x in range(m):
        # 投资第一个项目
        dp[0][x] = ABC[0][x]
        status[0][x] = x

    # 投资前i个项目
    for i in range(1, n):

        # 前i个项目总投入的钱数j
        for j in range(m):

            # 投资当前项目i的钱数
            for k in range(j):

                tmp = ABC[i][k] + dp[i - 1][j - k]
                if tmp > dp[i][j]:
                    # 更新当前的最优解
                    dp[i][j] = tmp
                    # 更新标志函数
                    status[i][j] = k
    return dp[n - 1][m - 1]


def print_result(n, m):
    inv = [0] * n
    inv[n - 1] = status[n - 1][m - 1]
    for i in range(n - 2, -1, -1):
        t = 0
        for j in range(n - 1, i, -1):
            t += inv[j]
        inv[i] = status[i][m - t]

    for x in range(n):
        # print("Invest", inv[x], "for project", x + 1)
        pass


def dp_blocks(i, j, k):
    if i == j:
        d[i][j][k] = (length[j] + k) ** 2
        return d[i][j][k]

    # 备忘录状态查询
    if d[i][j][k] > 0:
        return d[i][j][k]

    # 暂时先取第一种方式的结果作为d[i][j][len]的值
    d[i][j][k] = dp_blocks(i, j - 1, 0) + (length[j] + k) * (length[j] + k)

    # 按照第二种方式计算，并根据情况更新d[i][j][len]的值
    for p in range(i, j):
        if color[p] == color[j]:
            tmp = dp_blocks(i, p, length[j] + k) + dp_blocks(p + 1, j - 1, 0)
            if tmp > d[i][j][k]:
                d[i][j][k] = tmp

    return d[i][j][k]


if __name__ == '__main__':
    color = [0, 1, 2, 3, 1]
    length = [0, 1, 4, 3, 1]

    # 初始化一个足够大的区域
    d = [[[0] * 16] * 16] * 16
    # print(d)

    score = dp_blocks(1, 4, 0)
    print(score)








    ############
    n = 3
    m = 6
    ABC = [A, B, C]
    dp = [[0] * m] * n
    status = [[0] * m] * n

    benefit = investment(n=n, m=m)
    # print("Total benefit :", benefit)
    print_result(3, 6)
