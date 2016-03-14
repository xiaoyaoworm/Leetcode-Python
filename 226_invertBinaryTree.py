# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None;
        else:
            l = self.invertTree(root.left)
            r = self.invertTree(root.right)
            root.right = l
            root.left = r
            return root