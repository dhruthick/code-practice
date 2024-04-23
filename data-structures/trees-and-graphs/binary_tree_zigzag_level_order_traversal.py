# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    MEDIUM: 103
    Given the root of a binary tree, return the zigzag level order 
    traversal of its nodes' values. (i.e., from left to right, then 
    right to left for the next level and alternate between).
    '''
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        answer = []
        zig = True
        if not root:
            return answer
        while q:
            num_nodes = len(q)
            answer.append([x.val for x in q] if zig else [x.val for x in reversed(q)])
            for i in range(num_nodes):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            zig = not zig
        return answer