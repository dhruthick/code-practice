# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    MEDIUM: 1302
    Given the root of a binary tree, return the sum of values of 
    its deepest leaves.
    '''
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        q = [root]
        while q:
            num_nodes = len(q)
            answer = sum([node.val for node in q])
            for i in range(num_nodes):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return answer
            