"""

    将 M 个同样的糖果放在 N 个同样的篮子里，允许有的篮子空着不放，共有多少种不同的分法？
    比如，把 7 个糖果放在 3 个篮子里，共有 8 种分法（每个数表示篮子中放的糖果数，数的个数为篮子数）：
        1 1 5
        1 2 4
        1 3 3
        2 2 3
        2 5 0
        3 4 0
        6 1 0
        7 0 0
    注意：相同的分布，顺序不同也只算作一种分法，如 7 0 0、0 7 0 和 0 0 7 只算作一种。

输入包含二个正整数 M 和 N，以(,)分开，M 表示有几个同样的糖果，N 表示有几个同样的篮子 M与N范围：1 <= M，N <= 100。

输出一个正整数 K，表示有多少种分法。

输入样例

    7,3

输出样例

    8

"""

# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here

    # return 'your_answer'

    m_t, n_k = line.strip().split(' ')
    m_t = int(m_t)
    n_k = int(n_k)

    min_t_ = m_t / n_k
    min_t = m_t // n_k

    m_1 = m_t

    if n_k <= 1:
        return n_k

    ss = []

    def f():
        if min_t < min_t_:
            return m_1 > min_t
        else:
            return m_1 >= min_t

    # change = 0
    while f():

        s_list = [m_1] + [0 for __ in range(1, n_k)]

        while sum(s_list) < m_t:

            for i in range(1, n_k):
                s_list[i] = m_t - sum(s_list)

                # 限制排序
                if s_list[i - 1] < s_list[i]:
                    s_list[i] = s_list[i - 1]

                # while s_list[i] >= 2:

        # print(s_list)
        ss.append(s_list)

        from copy import deepcopy
        c_list = deepcopy(s_list)
        for x in range(1, n_k-1):
            print(c_list)
            x_ = 1
            while x_ < n_k-1:
                while c_list[x] > 1:
                    if c_list[x] - 1 >= c_list[x + 1] + 1:
                        # change += 1
                        c_list[x] = c_list[x] - 1
                        c_list[x + 1] = c_list[x + 1] + 1
                        print(c_list)
                        ss.append(c_list)
                    else:
                        break
                x_ += 1
                print(x)
        m_1 -= 1
    print(ss)

    # for i in range(len(ss)):
    #
    #     for x in range(1, len(ss[i])-1):
    #
    #         while ss[i][x] >= 1:
    #             if ss[i][x] - 1 >= ss[i][x + 1] + 1:
    #                 change += 1
    #                 ss[i][x] = ss[i][x] - 1
    #                 ss[i][x + 1] = ss[i][x + 1] + 1
    #                 print(ss[i])
    #             else:
    #                 break

    print(ss)
    return len(ss)
    # return len(ss)+change


aa = solution("7 3")
print(aa)
