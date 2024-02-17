# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    102: MEDIUM
    Given the root of a binary tree, return the level order 
    traversal of its nodes' values. (i.e., from left to 
    right, level by level).
    '''
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = [root]
        while q:
            nodes = []
            level_length = len(q)
            for i in range(level_length):
                node = q.pop(0)
                nodes.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(nodes)
        return res