class Solution:

    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            ans1 = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            ans2 = self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)
            return ans1 or ans2
        return False


S = Solution()
