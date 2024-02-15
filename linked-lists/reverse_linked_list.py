# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    '''
    206: EASY
    Given the head of a singly linked 
    list, reverse the list, and return 
    the reversed list.
    '''
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        left = None
        curr = head
        right = head.next
        while right:
            curr.next = left
            left = curr
            curr = right
            right = right.next
        curr.next = left
        return curr