class Solution:
    def largestSumAfterKNegations(self, A: list, K: int) -> int:

        # 分组
        M = []
        m = []
        aa = None
        for a in A:
            if a > 0:
                M.append(a)
            elif a < 0:
                m.append(a)
            else:
                aa = a

        S_M = sum(M)
        lm = len(m)

        if M:
            M.sort()
            # lM = len(M)

        if m:
            m.sort()

            if K <= lm:
                return S_M - sum(m[:K]) + sum(m[K:])
            elif K > lm:
                if aa is None and (K - lm) % 2:
                    return S_M - sum(m) - 2*min(M+[-x for x in m])
                else:
                    return S_M - sum(m)

        if aa is None and (K-lm) % 2:
            return sum(M[1:]) - M[0]
        else:
            return S_M

