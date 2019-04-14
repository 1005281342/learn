class Solution:
    def divisorGame(self, N: int) -> bool:

        # 能使得鲍勃选择2，爱丽丝选择最后一个1
        if N == 2:
            return True
        elif N > 3 and (N % 2 == 0 or N % 3 == 0):
            return True
        else:
            return False


S = Solution()
res = S.divisorGame(5)
print(res)
