# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):

        self.a = set()

    def make_data(self, root):

        if root:

            self.a.add(root.val)
            self.a.add(root.left.val)
            self.a.add(root.right.val)

            self.make_data(root.left)

            self.make_data(root.left)

    def make_data_2(self, root):

        if root:

            self.make_data(root.left)

            self.make_data(root.left)
            self.a.add(root.val)


    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.make_data(root)
        return len(self.a) < 2



aa = Solution()
b = aa.isUnivalTree([1,1,1,1,1,None,1])
print(b)