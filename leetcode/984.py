class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """

        if A < B:

            s_list = []
            while A>0 and B>0:
                A -= 1
                B -= 1
                s_list.append('ba')

            index = 0
            while B > 0:
                B -= 1
                try:
                    s_list[index] = 'b' + s_list[index]
                except:
                    s_list.append('b')
                index += 1

            return ''.join(s_list)

        else:

            s_list = []
            while A > 0 and B > 0:
                A -= 1
                B -= 1
                s_list.append('ab')

            index = 0
            while A > 0:
                A -= 1
                try:
                    s_list[index] = 'a' + s_list[index]
                except:
                    s_list.append('a')
                index += 1

            return ''.join(s_list)


S = Solution()
a = S.strWithout3a3b(4, 1)
print(a)