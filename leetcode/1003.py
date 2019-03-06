class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        n = len(S)
        if n % 3:
            return False
        stack = []
        for i in range(n):
            index = ord(S[i]) - ord('a')
            if index == 2 and len(stack) > 1 and stack[-1] == 1 and stack[-2] == 0:
                stack.pop()
                stack.pop()
            else:
                stack.append(index)
        if stack:
            return False
        else:
            return True


S = Solution()

res = S.isValid("ababcbcabc")
print(res)