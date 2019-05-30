class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # mm = {x for x in range(nums[0], nums[0] + k + 10000)}
        #
        # h = sorted(list(mm - set(nums)))
        #
        # return h[k - 1]

        if k < nums[-1]:
            mm = {x for x in range(nums[0], nums[0] + k + 10000)}

            h = sorted(list(mm - set(nums)))

            return h[k - 1]
        else:
            return nums[-1]+k-(nums[-1]-nums[0]+1-len(nums))


S = Solution()
res = S.missingElement([1,2,9],  5)
print(res)