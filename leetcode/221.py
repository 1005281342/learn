#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (36.22%)
# Total Accepted:    3.2K
# Total Submissions: 8.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#
#

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 矩阵为空
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        w, h = len(matrix), len(matrix[0])
        # counters = [0 for __ in range(h)]
        counters = [0] * h
        max_size = 0

        for row in matrix:
            for i in range(h):
                if row[i] == "0":
                    counters[i] = 0
                else:
                    counters[i] += 1

            next_size = max_size + 1
            freq = 0  # 记录连续有几组值大于等于高度size
            for c in counters:
                if c >= next_size:
                    freq += 1
                else:
                    freq = 0
                if freq >= next_size:
                    max_size = next_size
                    break

        return max_size * max_size
