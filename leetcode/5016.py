class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        stack = []
        for s in S:
            if stack:
                if s == '(':
                    stack.append(s)
                    res += s

                elif s == ')':

                    stack.pop()
                    if stack:
                        res += s

            else:
                stack.append(s)
        return res

S = Solution()
aa = S.removeOuterParentheses("(()())(())(()(()))")
print(aa)