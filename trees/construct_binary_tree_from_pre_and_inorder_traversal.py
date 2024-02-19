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
        # preorder's first index giver root
        # root's index in inorder givex left and right subtree
        def build(left, right):
            nonlocal rootIndex
            if left > right:
                return None
            rootValue = preorder[rootIndex]
            root = TreeNode(rootValue)
            rootIndex += 1
            # left HAS TO be assigned before right
            root.left = build(left, index_map[rootValue] - 1)
            root.right = build(index_map[rootValue] + 1, right)
            return root
        rootIndex = 0
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i
        return build(0, len(preorder) - 1)
       