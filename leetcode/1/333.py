from math import ceil, floor


class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """

        nums = [float(s) for s in prices]
        # 获取小数部分
        # dot = sorted([float(s.replace(s.split('.')[0], '0')) for s in prices])
        # print(dot)
        print(nums)
        y = sum(nums)
        dis = float(format(y - target, '.3f'))
        y1 = sum([ceil(n) for n in nums])
        y2 = sum([floor(n) for n in nums])

        print(y, dis, y1, y2)
        if target < y2 or target > y1:
            return "-1"

        if target < y < y1:
            res = format(y1 - target, '.3f')
            a, b = res.split('.')
            if len(b) < 3:
                b = b+(3-len(b))*0
            return a+'.'+b
        elif y2 < y < target:
            res = format(target - y, '.3f')
            a, b = res.split('.')
            if len(b) < 3:
                b = b + (3 - len(b)) * 0
            return a + '.' + b
        return "-1"


S = Solution()
print(S.minimizeError(prices=["0.500", "2.800", "4.900"], target=8))
