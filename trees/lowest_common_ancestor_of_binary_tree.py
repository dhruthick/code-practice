# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    MEDIUM: 236
    Given a binary tree, find the lowest common ancestor (LCA) 
    of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest 
    common ancestor is defined between two nodes p and q as the 
    lowest node in T that has both p and q as descendants (where 
    we allow a node to be a descendant of itself).”
    
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left if left else right
        
        return dfs(root)