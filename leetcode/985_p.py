class Solution:

    def __init__(self):
        self.aa = {}
        self.bb = {}

    def f_l(self, A: list):

        for i in range(len(A)):
            if A[i] % 2 == 0:
                self.aa[i] = A[i]
            else:
                self.bb[i] = A[i]

    def sumEvenAfterQueries(self, A: list, queries: list) -> list:

        self.f_l(A)
        print(self.aa)
        res = []
        for qu in queries:

            val, index = qu
            A[index] += val
            print(self.aa)
            print(self.bb)
            if val % 2 == 0:
                if index in self.aa.keys():
                    self.aa[index] = A[index]
                    # res.append(res[-1]+val)
                else:
                    self.bb[index] = A[index]
                    # res.append(res[-1])
            else:  # 需要交换
                if index in self.aa.keys():

                    self.bb[index] = A[index]
                    del self.aa[index]
                else:
                    self.aa[index] = A[index]
                    del self.bb[index]
            res.append(sum(self.aa.values()))
            print(res)
        return res


S = Solution()
S.sumEvenAfterQueries([-10,4,0,1,7,-8,-3,-10,-2]
, [[-3,4],[3,8],[1,7],[10,6],[-9,7],[10,4],[3,3],[-4,1],[-8,2]])