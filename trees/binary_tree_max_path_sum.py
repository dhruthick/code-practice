# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    124: HARD
    The path sum of a path is the sum of the 
    node's values in the path.
    Given the root of a binary tree, return 
    the maximum path sum of any non-empty path.
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        # time and space - O(n)
        
        # post order traversal
        def subTreeGain(root):
            nonlocal max_sum
            if not root:
                return 0
            # gain from the left subtree
            left_gain = max(subTreeGain(root.left), 0)
            # gain from the right subtree
            right_gain = max(subTreeGain(root.right), 0)
            # track max, incase the max does not include the root but only one subtree
            max_sum = max(left_gain + right_gain + root.val, max_sum)
            # return gain when root is included
            return max(left_gain, right_gain) + root.val

        max_sum = -float('inf')
        max_sum_root = subTreeGain(root)
        return max_sum