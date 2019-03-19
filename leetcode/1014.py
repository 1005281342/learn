### 解题错误
class Solution:
    def shipWithinDays(self, weights: list, D: int) -> int:
        w_all = sum(weights)
        a = w_all // D
        print(a)

        res = [0] * D
        c = 0
        i = 0
        for w in weights:
            if w >= a:
                res[i] = w
                i += 1

            else:
                c += w
                if c >= a:
                    res[i] = c
                    i += 1

                    c = 0
                else:
                    res[i] = c

        s = sorted(res)
        print(s)
        c_0 = s.count(0)
        if not s[-1 - c_0]:
            return max(weights[:]+[s[-1]])
        return max([s[-1 - c_0]]+weights[:])


S = Solution()
res = S.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2], D=5)
print(res)
