class Solution:
    def largestPerimeter(self, A: list):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)

        A.sort(reverse=True)
        res = 0
        for x in range(l-2):
            if A[x+1]+A[x+2] > A[x]:
                res = A[x+1]+A[x+2]+A[x]
                break

        return res


if __name__ == '__main__':

    s = Solution()
    print(s.largestPerimeter([2,1,2]))
