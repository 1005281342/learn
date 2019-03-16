class Solution:

    def clumsy(self, N: int) -> int:
        status = False
        res_list = []
        while N > 0:
            res = N
            # print('N', N)
            N = N - 1
            # print(res)

            if N > 0:
                res *= N
                N -= 1
                # print(N)
                # print(res)
            if N > 0:
                res //= N
                N -= 1
                # print(N)
                # print(res)

            if N > 0 and status:
                res -= N
                N -= 1
                # print(N)
                # print(res)
            elif N > 0 and not status:
                res += N
                N -= 1

            # print('res', res)
            if not status:
                res_list.append(res)
                status = True
            else:
                res_list.append(-res)
        return sum(res_list)


S = Solution()
c = S.clumsy(10)
print(c)

"""
class Solution:
    def clumsy(self, n: int) -> int:
        s = ""
        for i in range(n):
            s += str(n-i)
            if i != n-1:
                if i%4 == 0:
                    s += "*"
                elif i%4 == 1:
                    s += "//"
                elif i%4 == 2:
                    s += "+"
                else:
                    s += "-"
        return eval(s)
"""
