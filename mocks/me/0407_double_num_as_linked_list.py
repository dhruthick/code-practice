# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    '''
    MEDIUM: 2816

    You are given the head of a non-empty linked list representing 
    a non-negative integer without leading zeroes.

    Return the head of the linked list after doubling it.
    '''
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse_ll(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        new_head = reverse_ll(head)
        carry = 0
        curr = new_head
        while curr:
            new_val = curr.val * 2 + carry
            curr.val = new_val % 10
            carry = new_val / 10
            curr = curr.next
        head = reverse_ll(new_head)
        if carry:
            temp = ListNode(1, head)
            return temp
        return head
        