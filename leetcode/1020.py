# class Solution:
#     def canThreePartsEqualSum(self, A: list) -> bool:
#
#         if len(A) < 3:
#             return False
#
#         a, b = 0, len(A) - 1
#         c = 0
#         while a + 1 < b:
#             if sum(A[:a + 1]) == sum(A[b:]) == sum(A[a + 1: b]):
#                 return True
#             elif sum(A[:a + 1]) < sum(A[b:]):
#                 a += 1
#                 c += 1
#             elif sum(A[:a + 1]) > sum(A[b:]):
#                 b -= 1
#                 c += 1
#             else:
#                 return False
#             # print(a + 1, b)
#         return False

class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:

        m = sum(A) // 3

        c_a = 0
        for a in range(len(A) - 2):
            c_a += A[a]
            if c_a == m:
                break
        c_b = 0
        for b in range(len(A) - 1, a, -1):
            c_b += A[b]
            if c_b == m:
                break

        if sum(A[:a + 1]) == sum(A[a + 1:b]) == sum(A[b:]):
            return True
        else:
            return False


S = Solution()
aa = S.canThreePartsEqualSum([0, 2, 1, 3, -6, 6, 7, 9, -1, 3, 2, 0, 1])
print(aa)
