# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    98: MEDIUM
    Given the root of a binary tree,
    determine if it is a valid binary search tree (BST).
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import math
        global tracker
        tracker = float('-inf')
        def inorder(node):
            global tracker
            if not node:
                return True
            if not inorder(node.left): return False
            if node.val <= tracker:
                return False
            tracker = node.val
            return inorder(node.right)
        return inorder(root)
        