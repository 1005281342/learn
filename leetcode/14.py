#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.10%)
# Total Accepted:    59.9K
# Total Submissions: 185.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:

        if not strs:
            return ''

        strs.sort(key=len)
        # print(strs)
        l = len(strs[0])
        # status = False
        # while l > 0 and not status:
        while l > 0:
            start = strs[0][:l]
            # print(start)
            count = 1
            for string in strs[1:]:
                if start != string[:l]:
                    l -= 1
                    break
                count += 1
            if count == len(strs):
                # status = False
                return start

        return ''


if __name__ == '__main__':
    S = Solution()
    res = S.longestCommonPrefix(["dog","racecar","car"])
    print(res)
