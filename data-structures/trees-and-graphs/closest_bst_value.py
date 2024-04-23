# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    EASY: 270
    Given the root of a binary search tree and a target value, return the value in the 
    BST that is closest to the target. If there are multiple answers, print the smallest.
    '''
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        return closest
            
