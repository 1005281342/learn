#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (39.02%)
# Total Accepted:    18.9K
# Total Submissions: 48.1K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数,使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如,给定数组 nums = [-1,2,1,-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#
# class Solution:
#
#     def b_min(self, a, b):
#         if abs(a) > abs(b):
#             return b
#         return a
#
#     def threeSumClosest(self, num: list, target: int):
#         #  初始化一个大数
#         s = 2 << 32
#         num.sort()
#         for i in range(len(num) - 2):
#             # 起始点与不重复的
#             if i == 0 or num[i] > num[i - 1]:
#                 left = i + 1
#                 right = len(num) - 1
#                 while left < right:
#                     if num[i] + num[left] + num[right] == target:
#
#                         return num[i] + num[left] + num[right]
#                         # s = self.b_min(s, target-(num[i]+num[left]+num[right]))
#                         # left += 1
#                         # right -= 1
#                         # while left < right and num[left] == num[left - 1]:
#                         #     left += 1
#                         # while left < right and num[right] == num[right + 1]:
#                         #     right -= 1
#                     elif abs(num[i] + num[left] + num[right]) < target:
#                         while left < right:
#                             s = self.b_min(s, (num[i] + num[left] + num[right])-target)
#                             left += 1
#                             if num[left] > num[left - 1]:
#                                 break
#                     else:
#                         while left < right:
#                             s = self.b_min(s, (num[i] + num[left] + num[right]) - target)
#                             right -= 1
#                             if num[right] < num[right + 1]:
#                                 break
#         return s+target

class Solution:

    # def b_min(self, a, b):
    #     if abs(a) > abs(b):
    #         return b
    #     return a

    def b_min(self, a, b):
        if abs(a) > abs(b):
            return b
        return a

    def threeSumClosestP(self, nums: list, target: int):
        # nums.sort()
        m_l = len(nums)
        s = 1 << 32
        for i in range(m_l-2):
            for j in range(i+1, m_l-1):
                for k in range(j+1, m_l):
                    s = self.b_min(s, nums[i]+nums[j]+nums[k]-target)
                    # print(s)

        return s + target

    def threeSumClosest(self, num: list, target: int):
        num.sort()
        m_l = len(num)

        if m_l <= 3:
            return sum(num)

        if m_l <= 140:
            return self.threeSumClosestP(num, target)

        res_d = dict()
        # 初始化一个很远的点在右边
        s = 1 << 32
        for i in range(m_l - 2):
            if i == 0 or num[i] > num[i - 1]:
                left = i + 1
                right = m_l - 1
                # 点重合
                if num[i] + num[left] + num[right] == target:
                    return num[i] + num[left] + num[right]
                # 点在左边
                elif num[i] + num[left] + num[right] < target:
                    while left < right:
                        # s = self.b_min(s, num[i] + num[left] + num[right] - target)
                        p = abs(num[i] + num[left] + num[right] - target)
                        if p < s:
                            s = p
                            res_d[p] = num[i] + num[left] + num[right]
                        left += 1
                        # print(s)

                        # if num[left] > num[left - 1]:
                        #     break
                # 点在右边
                else:
                    while left < right:
                        # s = self.b_min(s, num[i] + num[left] + num[right] - target)
                        p = abs(num[i] + num[left] + num[right] - target)
                        if p < s:
                            s = p
                            res_d[p] = num[i] + num[left] + num[right]
                        right -= 1
                        # if num[right] < num[right + 1]:
                        #     break
        return res_d[min(res_d.keys())]

# class Solution:
#
#     def b_min(self, a, b):
#         if abs(a) > abs(b):
#             return b
#         return a
#
#     def threeSumClosest(self, nums: list, target: int):
#         # nums.sort()
#         m_l = len(nums)
#         s = 1 << 32
#         for i in range(m_l-2):
#             for j in range(i+1, m_l-1):
#                 for k in range(j+1, m_l):
#                     s = self.b_min(s, nums[i]+nums[j]+nums[k]-target)
#                     # print(s)
#
#         return s + target


S = Solution()
# print(S.threeSumClosest([0, 2, 1, -3], 1))  # 0
print(S.threeSumClosest([-1, 2, 1, -4], 1))   # 2
# print(S.threeSumClosest([1,2,4,8,16,32,64,128], 82))   # 82
print(S.threeSumClosest([56,57,-47,-14,23,31,20,39,-51,7,-4,43,-53,32,24,56,-28,90,-75,-6,21,-100,41,-84,95,95,44,84,70,-22,-86,-6,90,-87,65,-28,-29,-94,98,-28,-100,23,-25,6,-56,-54,-5,53,-88,-25,-31,-71,-13,-62,73,-35,-78,16,99,97,84,-27,-43,-50,18,-16,-61,7,-17,16,-92,28,43,-38,-33,-27,84,-72,-100,-91,-97,-99,59,-63,73,99,98,-100,-37,-80,3,18,93,-81,12,-75,-43,99,10,10,-6,13,0,76,-82,-5,27,-38,-81,77,-55,-100,90,-32,-25,-15,-16,68,-6,87,65,-38,82,78,-61,87,-72,46,50,-60,86,39,69,85,-49,28], -289))   # 82
