# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    572: EASY
    Given the roots of two binary trees root 
    and subRoot, return true if there is a subtree 
    of root with the same structure and node 
    values of subRoot and false otherwise.
    '''
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # time - O(mn), space O(m + n)
        # use the solution for SAME TREE
        def traverse_trees(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return traverse_trees(root1.right, root2.right) and traverse_trees(root1.left, root2.left)
        
        # BFS
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if traverse_trees(node, subRoot):
                return True
        return False
        