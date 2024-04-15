# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    EASY: 1469
    In a binary tree, a lonely node is a node that is the only 
    child of its parent node. The root of the tree is not lonely 
    because it does not have a parent node.

    Given the root of a binary tree, return an array containing 
    the values of all lonely nodes in the tree. Return the list 
    in any order.
    '''
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def preorder(node):
            if not node:
                return
            if node.left and not node.right:
                answer.append(node.left.val)
            if node.right and not node.left:
                answer.append(node.right.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return answer