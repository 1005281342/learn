"""

    我是一个爱吃香蕉的强迫症。今天我要去水果店论筐买香蕉。 现在水果店有好多筐香蕉，我的要求是买回来的每一筐里必须有相同数量的香蕉。

    为了实现这个目标，你可以每次做两件事情。
        1）放弃框里的一部分香蕉
        2）连筐带香蕉放弃一整筐

    我想知道我能得到最多多少香蕉。


i    以空格分割的多个正整数，每个正整数表示一筐香蕉的总香蕉数

o    最多能得到的香蕉数

输入样例

    1 2 3
    5 0 29 14

输出样例

    4
    29

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
    nums = [int(x) for x in line.strip().split(' ')]
    nums.sort()

    s = set()
    for x in range(len(nums)):

        s.add(nums[-(x+1)]*(x+1))

    return max(s)


aa = solution("5 0 29 14")
print(aa)
