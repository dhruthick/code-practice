'''
Given the root of a binary tree, imagine yourself standing on 
the right side of it, return the values of the nodes you 
can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode):
    right_view = []
    if not root:
        return right_view
    queue = [root]
    while queue:
        length = len(queue)
        for i in range(length):
            node = queue.pop(0)
            if i == length - 1:
                right_view.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return right_view


print(rightSideView([1,2,3,None,5,None,4]))
print(rightSideView([1,None, 3]))
print(rightSideView([]))