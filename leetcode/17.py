#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (47.70%)
# Total Accepted:    18K
# Total Submissions: 37.5K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list:

        # 创建字母对应的字符列表的字典
        dic = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z'],
               }
        # 存储结果的数组
        ret_str = []
        if len(digits) == 0:
            return []
        # 递归出口，当递归到最后一个数的时候result拿到结果进行for循环遍历
        if len(digits) == 1:
            return dic[int(digits[0])]
        # 递归调用, 每次移动一位
        result = self.letterCombinations(digits[1:])
        # result是一个数组列表，遍历后字符串操作，加入列表
        for r in result:
            for j in dic[int(digits[0])]:
                ret_str.append(j + r)
        return ret_str

        # if len(digits) == 1:
        #     return list(d[digits])
        #
        # x = ['']
        # for char in digits:
        #     if char in {'7', '9'}:
        #         x *= 4
        #     else:
        #         x *= 3
        # # print(x)
        # # l_x = len(x)
        # for v in digits:
        #     l_v = len(d[v])
        #     # print(l_v)
        #     for i in range(l_v):
        #         for ii, j in enumerate(d[v]):
        #             # print(j)
        #             x[i * l_v + ii] += j

        # for bb in product(x):
        #     print(bb)
        # return x


S = Solution()
print(S.letterCombinations("23"))
