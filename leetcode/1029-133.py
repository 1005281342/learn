class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        length = len(costs) >> 1
        count = 0
        chas = [-abs(a - b) for a, b in costs]
        c = 0
        d = 0
        while c < length or d < length:
            v = min(chas)
            i = chas.index(v)
            if chas[i] > 0:
                break
            a, b = costs[i]
            print(a, b)
            if c < length and (a < b or d == length):
                count += a
                c += 1
            elif d < length:
                count += b
                d += 1
            chas[i] = 1

        return count


S = Solution()
res = S.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
print(res)
