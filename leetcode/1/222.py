class Solution(object):

    def get_manhattan(self, a, b):

        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        d = dict()
        ans = [None] * len(bikes)

        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                k = self.get_manhattan(a=worker, b=bike)
                if d.get(k):
                    d[k].append((i, j))
                else:
                    d[k] = [(i, j)]
        # print(d)
        for k in sorted(list(d.keys())):
            # print(k)
            for v in sorted(d[k]):
                i, j = v
                # print(i)
                if i in ans or ans[j] is not None:
                    continue
                ans[j] = i
        print(ans)


S = Solution()
S.assignBikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]])
