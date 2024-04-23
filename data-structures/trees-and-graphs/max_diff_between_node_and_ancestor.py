# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    MEDIUM: 1026
    Given the root of a binary tree, find the maximum value v for which 
    there exist different nodes a and b where v = |a.val - b.val| and a 
    is an ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b 
    or any child of a is an ancestor of b.
    '''
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, max_val, min_val):
            if not node:
                return
            val = node.val
            self.ans = max(abs(max_val - val), abs(min_val - val), self.ans)
            dfs(node.right, max(val, max_val), min(val, min_val))
            dfs(node.left, max(val, max_val), min(val, min_val))

        dfs(root, root.val, root.val)
        return self.ans
