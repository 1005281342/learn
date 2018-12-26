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

    def candy(ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0:
            return 0
        candies = [0]*n

        # 先从左向右遍历，初步给每位小朋友赋糖果初值
        for i in range(n):
            if i == 0:
                candies[i] = 1
            else:
                if ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1]+1
                else:
                    candies[i] = 1
        for i in range(n-1, -1, -1):
            if i == n-1:
                continue
            else:
                if ratings[i] > ratings[i+1]:
                    candies[i] = max(candies[i], candies[i+1]+1)
                else:
                    continue
        res = sum(candies)
        return res

    return candy(nums)


aa = solution("19,9,35,74,22")
print(aa)
