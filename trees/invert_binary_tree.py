# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    226: EASY
    Given the root of a binary tree,
    invert the tree, and return its root.
    '''
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # recursively invert and go down the tree
        if not root:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root