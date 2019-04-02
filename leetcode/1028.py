class Solution:

    def baseNeg2(self, N: int) -> str:
        x_list = [(-2) ** x for x in range(N + 1, -1, -1)]

        rc = ''
        for i, c in enumerate(x_list):
            print(c)
            if c + N < 0 or c / N > 2:
                continue
            elif N > 0 and c - N == 0:
                rc += '1'
                rc += '0' * (len(x_list) - 1 - i)
                break
            elif N < 0 and c + N == 0:
                rc += '1'
                rc += '0' * (len(x_list) - 1 - i)
                break

            elif N > 0 and N - c > 0:
                N -= c
                rc += '1'
            elif N > 0 and N + c > 0:
                N += c
                rc += '1'
            else:
                rc += '0'
        return rc


S = Solution()
r = S.baseNeg2(5)
print(r)
