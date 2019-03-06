from collections import deque


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        ans = 0
        now = 0
        if K == 0:
            for i in range(n):
                if A[i] == 0:
                    ans = max(now, ans)
                    now = 0
                else:
                    now += 1
            return max(ans, now)
        q = deque()
        for i in range(n):
            if A[i] == 0:
                if len(q) < K:
                    q.append(i)
                    now += 1
                else:
                    l = q.popleft()
                    q.append(i)
                    ans = max(ans, now)
                    now = i - l
            else:
                now += 1
        return max(ans, now)
