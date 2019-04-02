class Solution:

    def res(self, s):
        return int(s, 2) % 5 == 0

    def prefixesDivBy5(self, A: list) -> list:
        m = '0b'
        res_list = []
        for c in A:
            m += str(c)
            res_list.append(self.res(m))

        return res_list


S = Solution()
print(S.prefixesDivBy5([0,1,1]))