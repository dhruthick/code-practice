# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    104: EASY
    Given the root of a binary tree, return its maximum depth.
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(node):
            if node==None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        return height(root)
        