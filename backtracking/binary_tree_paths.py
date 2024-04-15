# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    EASY: 257
    Given the root of a binary tree, return all root-to-leaf paths in any order.

    A leaf is a node with no children.
    '''
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def format_path(path):
            return '->'.join(path)
        def backtrack(node, path):
            if not node.left and not node.right:
                answer.append(format_path(path))
                return
            if node.left:
                path.append(str(node.left.val))
                backtrack(node.left, path)
                path.pop()
            if node.right:
                path.append(str(node.right.val))
                backtrack(node.right, path)
                path.pop()
        
        backtrack(root, [str(root.val)])
        return answer