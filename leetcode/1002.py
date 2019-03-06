from functools import reduce
from collections import Counter


class Solution:
    def commonChars(self, A: list) -> list:

        t = []
        s = set()
        length = len(A)

        tmp = [Counter(it) for it in A]

        # print(tmp)

        for i in range(length):
            if not s:
                s = s | set(tmp[i].keys())
            else:
                s = s & set(tmp[i].keys())
        # print(s)
        for char in s:
            m = 2 << 16
            for c in tmp:
                if c[char] < m:
                    m = c[char]
            for __ in range(m):
                t.append(char)

        return t


class Solution2(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())


S = Solution()
res = S.commonChars(["bbddabab", "cbcddbdd", "bbcadcab", "dabcacad", "cddcacbc", "ccbdbcba", "cbddaccc", "accdcdbb"])
print(res)
