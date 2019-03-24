class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for x in range(N, -1, -1):
            # print(x)
            # print(bin(x)[2:])
            if bin(x)[2:] not in S:
                return False
        return True


S = Solution()
s = S.queryString(S="0110", N=4)
print(s)