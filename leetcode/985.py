class Solution:

    def sum_o(self, a_list: list) -> int:

        return sum([x for x in a_list if x%2==0])

    def sumEvenAfterQueries(self, A: list, queries: list) -> list:

        res = []
        for qu in queries:
            A_T = A
            val, index = qu
            A_T[index] += val

            res.append(self.sum_o(A_T))

        return res
