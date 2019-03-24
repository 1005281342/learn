# class Solution:
#     def maxScoreSightseeingPair(self, A: list) -> int:
#
#         l = len(A)
#         if l < 2:
#             return 0
#         x = 0
#         if l > 4000:
#             # x = max(A[0], A[-1], A[l//2], A[l//4], A[l//8], A[l//16], A[l//32], A[l//64])
#             x = max(A) - 50
#         s = set()
#         for i in range(l - 1):
#             if A[i] < x:
#                 continue
#             else:
#                 for j in range(i + 1, l):
#                     if A[j] < x:
#                         continue
#                     elif A[i] + A[j] + i - j > x:
#                         s.add(A[i] + A[j] + i - j)
#
#         return max(s)
#
#
# S = Solution()
# aa = S.maxScoreSightseeingPair([])
# print(aa)


# class Solution:
#     def maxScoreSightseeingPair(self, A: list) -> int:
#
#         l = len(A)
#         if l < 2:
#             return 0
#
#         x = 0
#         if l > 4000:
#             # x = max(A[0], A[-1], A[l//2], A[l//4], A[l//8], A[l//16], A[l//32], A[l//64])
#             x = max(A) - 100
#
#         tt = sorted([(v, i) for i, v in enumerate(A) if v > x], reverse=True)
#         s = {0, }
#         for m in range(len(tt) - 1):
#
#             for n in range(m+1, len(tt)):
#
#                 s.add(tt[m][0]+tt[n][0]+tt[m][1]-tt[n][1])
#
#         return max(s)


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        last = 0
        ans = 0
        for i in range(n):
            last -= 1
            ans = max(ans, A[i] + last)
            last = max(last, A[i])
        return ans

S = Solution()
res = S.maxScoreSightseeingPair([1,2,3,4,5,6])
print(res)