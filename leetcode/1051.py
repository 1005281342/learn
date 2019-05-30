class Solution:
    def heightChecker(self, heights: list) -> int:

        c = 0
        for a, b in zip(heights, sorted(heights)):

            if a != b:
                c += 1

        return c


S = Solution()
print(S.heightChecker([1,1,4,2,1,3]))