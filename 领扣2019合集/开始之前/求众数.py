"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
"""


class Solution:
    def majorityElement(self, nums: list) -> int:
        res_len = len(nums) >> 1
        tmp = dict()
        for num in nums:
            if num in tmp.keys():
                tmp[num] += 1
            else:
                tmp[num] = 1
            if tmp[num] > res_len:
                return num
