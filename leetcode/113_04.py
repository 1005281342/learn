import math
import collections


class Solution(object):

    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = collections.defaultdict(set)
        factors = collections.defaultdict(set)

        def factor(n):
            nums[n].add(n)
            factors[n].add(n)
            for i in range(2, int(math.sqrt(n)) + 1, 1):
                if n % i == 0:
                    nums[i].add(n)
                    nums[n / i].add(n)
                    factors[n].add(i)
                    factors[n].add(n / i)

        for n in A:
            factor(n)

        A = set(A)
        res = 1

        while A:
            q = [A.pop()]
            i = 0
            while i < len(q):
                n = q[i]
                i += 1
                for f in factors[n]:
                    if f in nums:
                        for m in nums[f]:
                            if m in A:
                                q.append(m)
                                A.remove(m)
                        del nums[f]
            res = max(res, len(q))

        return res
