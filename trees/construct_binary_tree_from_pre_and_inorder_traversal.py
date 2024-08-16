# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    '''
    105: MEDIUM
    Given two integer arrays preorder and inorder 
    where preorder is the preorder traversal of a 
    binary tree and inorder is the inorder 
    traversal of the same tree, construct and 
    return the binary tree.
    '''
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # time and space - O(n)
    def build_tree(self, left, right):
        if left > right:
            return None
        rootval = self.preorder[self.root_index]
        self.root_index += 1
        root = TreeNode(rootval)
        root.left = self.build_tree(left, self.index_map[rootval] - 1)
        root.right = self.build_tree(self.index_map[rootval] + 1, right)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.index_map = {}
        for i, val in enumerate(inorder):
            self.index_map[val] = i
        self.root_index = 0
        return self.build_tree(0, len(preorder) - 1)
       