import itertools


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ps = itertools.permutations(A)
        ma, res = -1, ""
        for p in ps:
            h = p[0] * 10 + p[1]
            m = p[2] * 10 + p[3]
            if h >= 24 or m >= 60: continue
            if 60 * h + m > ma:
                ma = 60 * h + m
                res = '%02d:%02d' % (h, m)
        return res


class Solution2:

    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = []
        for i in range(4):
            A[0], A[i] = A[i], A[0]
            for j in range(1, 4):
                A[1], A[j] = A[j], A[1]
                for k in range(2, 4):
                    A[2], A[k] = A[k], A[2]
                    ans.append(str(A[0]) + str(A[1]) + str(A[2]) + str(A[3]))
                    A[2], A[k] = A[k], A[2]
                A[1], A[j] = A[j], A[1]
            A[0], A[i] = A[i], A[0]
        ans.sort(reverse=True)

        for i in ans:
            if int(i[:2]) < 24 and int(i[2:]) < 60:
                return i[:2] + ':' + i[2:]
        return ''


S = Solution()
print(S.largestTimeFromDigits([2, 0, 6, 6]))
