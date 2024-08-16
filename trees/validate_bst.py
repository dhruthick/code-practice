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
    # time and space - O(n)
    def __init__(self):
        self.prev = - float('inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left): return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        if not self.isValidBST(root.right): return False
        return True
        