class Solution:

    def count_l(self, a_list: list):

        a, b = a_list

        return a*a + b*b

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = list()
        tmp = dict()
        for point in points:
            l = self.count_l(point)
            if not tmp.get(l):
                m.append(l)
                tmp[l] = [point]
            else:
                tmp[l].append(point)

        m.sort()
        res = []
        for x in m:
            if len(res) == K:
                break
            for a in tmp[x]:
                res.append(a)
                if len(res) == K:
                    break

        return res


if __name__ == '__main__':

    s = Solution()
    print(s.kClosest(points = [[1,3],[-2,2]], K = 1))