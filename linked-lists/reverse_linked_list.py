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
        # time - O(n), space - O(1)
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev