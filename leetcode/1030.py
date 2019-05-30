class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        res = []
        for i in range(R):
            for j in range(C):
                res.append([i, j])
        res = sorted(res, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return res


S = Solution()
res = S.allCellsDistOrder(R=3, C=4, r0=0, c0=1)
print(res)
s = [[0, 1], [0, 0], [0, 2], [1, 1], [0, 3], [1, 0], [1, 2], [2, 1], [1, 3], [2, 0], [2, 2], [2, 3]]
