class Solution:

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        a = max(A)
        return A.index(a)
