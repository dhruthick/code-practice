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
        # time - O(n), space - O(logn), worst case O(n)
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        