class Solution:
    def bitwiseComplement(self, N: int) -> int:

        d = {
            1: 0,
            0: 1
        }

        def to2(N: int):
            s = []
            m, n = N // 2, N%2
            # print(m, n)
            s.append(n)
            while m > 0:
                m, n = m // 2, m % 2
                # print(m, n)
                s.append(n)
            return s
            # return ''.join(reversed(s))

        res = to2(N)
        # print(res)
        res_b = [2**i*d[x] for i, x in enumerate(res)]

        return sum(res_b)
C = Solution()
a = C.bitwiseComplement(5)
print(a)