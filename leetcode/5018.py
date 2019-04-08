class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        # p_list = []
        # s = ''
        # for char in pattern:
        #     if ord(char) <= 90:
        #         if s:
        #             p_list.append(s)
        #         s = ''
        #     s += char
        # p_list.append(s)
        # print(p_list)
        p_list = list(pattern)
        res = []
        for querie in queries:
            st = False
            for i, p in enumerate(p_list):
                if p in querie:
                    querie = querie.replace(p, '', 1)
                else:
                    res.append(False)
                    st = True
                    break

                if i > 0 and p_list[i - 1] in querie:
                    res.append(False)
                    st = True
                    break

            if not st:
                for char in querie:
                    if ord(char) <= 90:
                        res.append(False)
                        st = True
                        break
            if not st:
                res.append(True)
        return res


S = Solution()
r = S.camelMatch(["CompetitiveProgramming","CounterPick","ControlPanel"],
                 "CooP"
                 )


print(r)
