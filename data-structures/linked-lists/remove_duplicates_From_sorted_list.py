# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    EASY: 83
    Given the head of a sorted linked list, delete all duplicates such that each 
    element appears only once. Return the linked list sorted as well.
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # base case
      if not head or not head.next:
        return head
      
      t = head

      while t and t.next:
        if t.val == t.next.val:
            t.next = t.next.next
        else:
            t = t.next
      
      return head