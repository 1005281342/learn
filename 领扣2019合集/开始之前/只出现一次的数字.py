class Solution:
    def singleNumber(self, nums: list) -> int:
        if nums:
            nums.sort()
        while nums:
            if nums:
                a = nums.pop()
            else:
                return b
            if nums:
                b = nums.pop()
            else:
                return a
            if a != b:
                return a