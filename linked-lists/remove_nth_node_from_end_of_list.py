# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    19: MEDIUM
    Given the head of a linked list, remove
    the nth node from the end of the list
    and return its head.
    '''
    def removeNthFromEnd(self, head, n):
        # two pointer approach for a one-pass algorithm
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head