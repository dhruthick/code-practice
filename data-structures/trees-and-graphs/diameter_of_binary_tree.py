# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    EASY: 543
    Given the root of a binary tree, return the length of the 
    diameter of the tree.

    The diameter of a binary tree is the length of the longest 
    path between any two nodes in a tree. This path may or may 
    not pass through the root.

    The length of a path between two nodes is represented by 
    the number of edges between them.
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        max_height = dfs(root)

        return self.diameter