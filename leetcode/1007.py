class Solution:

    def res(self, a, b):
        count = 0
        for i in range(1, len(a)):
            if a[i] != a[0] and b[i] != a[0]:
                return -1
            elif a[i] != a[0]:
                a[i] = b[i]
                count += 1
        return count

    def minDominoRotations(self, A: list, B: list) -> int:

        return max(self.res(A[:], B[:]), self.res(B[:], A[:]))


S = Solution()
print(S.minDominoRotations([1,2,1,1,1,2,2,2],[2,1,2,2,2,2,2,2]))
