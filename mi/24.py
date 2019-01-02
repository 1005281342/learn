"""

描述

一箱失落多年的宝藏被两位海盗找到，宝箱里的一堆大小与重量各不相同的金块。 他们称出了每个金块的重量，但是如何如何平分这些金子却令他们十分头疼。
程序员们，你能告诉两位海盗，他们能否平分这箱宝藏么？
假设宝箱里有三块金子，重量分别为：1,2,3。则他们可以平分这些金子：1+2=3 又假设宝箱里有四块金子，重量分别为：1,2,6,4。则他们无法找到平分的方法

输入

    一行由逗号分隔的 N 个无序正整数（0<N<100），每个正整数表示每块金子的重量 W（0<W<10000）。

输出

    字符串true或false，表示海盗们能否平分这些金子

输入样例

1,2,3
1,2,6,4
1,6,8,3,5,9
10,5,8,6,20,13,7,11

输出样例

true
false
true
true

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

    nums = [int(x) for x in line.strip().split(',')]
    nums.sort()
    print(nums)

    len_nums = len(nums)
    if len_nums <= 1:
        return 'false'

    elif len_nums == 2 and nums[0] != nums[1]:
        return 'false'

    elif len_nums == 2 and nums[0] == nums[1]:
        return 'true'

    elif sum(nums) % 2 == 1:
        return 'false'

    else:

        average = sum(nums) // 2
        # num_j = []
        # num_o = []
        A = []
        B = []

        for num in nums:

            if sum(B) >= sum(A):
                A.append(num)
            else:
                B.append(num)
            # if num % 2 == 1:
            #     num_j.append(num)
            # else:
            #     num_o.append(num)

            if num == average:
                return 'true'
            elif num > average:
                return 'false'
        print(A)
        print(B)
        if sum(A) == sum(B) and A:
            return 'true'

        m = min(len(A), len(B))
        n = 0
        while n < m:
            for i in range(n, m):
                A[i], B[i] = B[i], A[i]
                if sum(A) == sum(B):
                    return 'true'
            print()
            n += 1


if __name__ == '__main__':

    aa = solution("10,5,8,6,20,13,7,11")
    print(aa)

    """
        var g_channels = window.g_channels = {
        201: {
            id: 201,
            name: '喜越国内'
        },
        203: {
            id: 203,
            name: '喜越国际'
        },
        293: {
            id: 293,
            name: 'Ctrip天驴国外'
        },
        294: {
            id: 294,
            name: 'Ctrip波妞海外'
        },
        296: {
            id: 296,
            name: 'Ctrip Ada'
        },
        1: {
            id: 1,
            name: '黑驴子'
        },
        2: {
            id: 2,
            name: '天旅'
        },
    
        3: {
            name: '星途国际',
            id: 3
        },
        4: {
            id: 4,
            name: '天宇'
        },
        5: {
            id: 5,
            name: '遨旅网'
        },
        6: {
            id: 6,
            name: '遨乐天下'
        },
        7: {
            id: 7,
            name: '遨房国际'
        },
        11: {
            id: 11,
            name: '飞猪'
        },
        19: {
            id: 19,
            name: '飞猪国际'
        },
    
    """
