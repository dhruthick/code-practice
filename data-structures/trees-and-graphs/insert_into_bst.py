# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    MEDIUM: 701
    You are given the root node of a binary search tree (BST) and a value to insert 
    into the tree. Return the root node of the BST after the insertion. It is 
    guaranteed that the new value does not exist in the original BST.

    Notice that there may exist multiple valid ways for the insertion, as long as 
    the tree remains a BST after insertion. You can return any of them.
    '''
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
        return TreeNode(val)