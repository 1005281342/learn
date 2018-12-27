"""
描述

市政府想在品罗路建一些基站，保证这条路上每个公司的员工都能享受到 Wi-Fi。
为了简化问题，我们将品罗路理解成一条直线，一个 Wi-Fi 基站为直线上的一个点。
基站的费用为 A + k*B，其中A为建立基站的固定费用，B 为覆盖每单位距离需要的费用，k 为覆盖半径。
如果在 a 点建立基站，覆盖半径为 k，那么位于 [a-k, a+k] 的公司都能享受到这个基站的服务。

现在给出每个公司的坐标，以及 A 和 B，求覆盖到所有公司需要的最小建设费用。

输入

    前两个整数是 A 和 B，然后是一个分号，然后是每个公司的坐标。（0 <= A, B <= 1000，0 <= 公司坐标 <= 1,000,000，坐标都为整数，公司数量 <= 2000）

输出

    一个浮点，表示最小建设费用，四舍五入到小数点后一位。

输入样例

    20 5;100 0 7

输出样例

    57.5
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

    x, y = line.strip().split(';')
    A, B = x.split(' ')
    A, B = int(A), int(B)
    nums = [int(x) for x in y.split(' ')]
    nums.sort()

    if A == 0:
        return 0.0
    if B == 0:
        return float(A)

    # 理想部署距离
    k_m = 2*A/B

    # j_s_list = []
    count = 0

    j_s = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1] <= k_m:
            j_s.append(nums[i])
        else:
            # j_s_list.append(j_s)
            count += A+(j_s[-1]-j_s[0])/2*B
            j_s = [nums[i]]
    # j_s_list.append(j_s)

    count += A+(j_s[-1]-j_s[0])/2*B
    return float(count)


if __name__ == '__main__':

    aa = solution("20 5;100 0 7 90")