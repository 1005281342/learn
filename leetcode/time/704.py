class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1

        imin, imax = 0, len(nums)
        while True:
            if imin >= imax:
                return -1
            midpoint = (imax+imin) // 2
            if nums[midpoint] > target:
                imax = midpoint
            elif nums[midpoint] < target:
                imin = midpoint
            else:
                return midpoint


S = Solution()
b = S.search([-1,0,3,5,9,12], 3)
print(b)


class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

        # L = len(nums)
        #
        # if not L:
        #     return -1
        # m = 0
        # n = L
        # i = L // 2
        # while i+1:
        #     if nums[i] > target:
