# class Solution:
#     def smallestRepunitDivByK(self, K: int) -> int:
#
#         for x in range(K, 2 << 32):
#             if x % K == 0 and set(list(str(x))) == {'1'}:
#                 return len(str(x))
#         return -1

# class Solution:
#     def smallestRepunitDivByK(self, K: int):
#
#         if K % 2 == 0:
#             return -1, 0
#         c = 0
#         while c < K:
#             c += 1
#             if int('1'*c) % K == 0:
#                 return c, int('1'*c) // K
#
#         return -1, 0


class Solution:
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        k = 9 * k
        m, n, x = k, k, 2
        while x * x <= n:
            if n % x == 0:
                m -= m // x
                while n % x == 0: n //= x
            x += 1
        if n > 1:
            m -= m // n
        r, x = -1, 1
        while x * x <= m:
            if m % x == 0:
                y = m // x
                if pow(10, x, k) == 1:
                    return x
                if pow(10, y, k) == 1:
                    r = y
            x += 1
        return r


S = Solution()
r = S.smallestRepunitDivByK(81103)
print(r)
