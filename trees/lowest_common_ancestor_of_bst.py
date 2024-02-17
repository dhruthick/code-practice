# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    235: MEDIUM
    Given a binary search tree (BST), find the lowest 
    common ancestor (LCA) node of two given nodes in the BST.
    '''
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while True:
            if p.val > node.val and q.val < node.val:
                return node
            elif p.val < node.val and q.val > node.val:
                return node
            elif p.val == node.val or q.val == node.val:
                return node
            elif p.val < node.val:
                node = node.left
            else:
                node = node.right