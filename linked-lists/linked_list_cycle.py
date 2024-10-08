# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    141: EASY
    Given head, the head of a linked list,
    determine if the linked list has a cycle in it.
    '''
    def hasCycle(self, head) -> bool:
        # Imagine two runners running on a track at different speed.
        # What happens when the track is actually a circle?

        # time - O(n), space - O(1)
        if not head:
            return False 

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False