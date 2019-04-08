# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from math import log

class Solution(object):

    def __init__(self):

        self.lst = []
        self.res = 0

    def add_char(self, root):

        if root.left:
            self.lst.append(root.left.val)
        if root.right:
            self.lst.append(root.right.val)
        if root.left:
            self.add_char(root.left)
        if root.right:
            self.add_char(root.right)


    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        try:
            self.lst.append(root.val)
            self.add_char(root)
        except:
            return 0

        if not self.lst:
            return 0

        length = len(self.lst)
        n = int(log(length+1, 2))
        an = 2**(n-1)
        print(n)

        for i in range(1, an+1):
            tmp = length - i
            hh = []
            while tmp:
                hh.append(self.lst[tmp])
                tmp = tmp >> 1
            if hh:
                self.res += int('0b' + ''.join(reversed(hh)), 2)
        print(self.res)
S = Solution()
S.sumRootToLeaf()