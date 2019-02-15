# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:

    def make(self, a, y_set):

        for x in range(a.start, a.end + 1):
            y_set.add(x)
        return y_set

    def intervalIntersection(self, A: list, B: list) -> list:

        mm = []
        aa = []
        bb = []
        for a in A:
            a_res = self.make(a, set())
            if a_res:
                aa.append(a_res)

        for b in B:
            b_res = self.make(b, set())
            if b_res:
                bb.append(b_res)

        for x in aa:

            for y in bb:
                res = x & y
                if res:
                    mm.append([min(res), max(res)])

        return mm
        # self.make(A, self.a)
        # self.make(B, self.b)
        #
        # print(self.a & self.b)


C = Solution()
a = C.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                       [[1, 5], [8, 12], [15, 24], [25, 26]])
print(a)