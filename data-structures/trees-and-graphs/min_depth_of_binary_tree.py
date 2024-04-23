# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    EASY: 111
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest 
    path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.
    '''
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if not node.left:
                return 1 + dfs(node.right)
            elif not node.right:
                return 1 + dfs(node.left)
            return 1 + min(dfs(node.left), dfs(node.right))

        return dfs(root)