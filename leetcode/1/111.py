class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s = {'0', '1', '6', '8', '9'}
        string = str(N)
        str_set = set(string)
        # 不能
        if s | str_set != s:
            return False

        if len(str_set) <= 1 and (not str_set & {'6', '9'}):
            return False

        rev = {
            '1': '1',
            '0': '0',
            '8': '8',
            '9': '6',
            '6': '9',
        }
        new = ''.join(reversed([rev[c] for c in list(string)]))
        # print(new)
        if new == string:
            return False
        return True


S = Solution()
res = S.confusingNumber(916)
print(res)
