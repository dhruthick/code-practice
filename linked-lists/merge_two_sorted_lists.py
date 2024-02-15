# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    '''
    21: EASY
    Merge the two lists into one sorted list.
    The list should be made by splicing together
    the nodes of the first two lists.
    
    Return the head of the merged linked list.
    '''
    def mergeTwoLists(self, list1, list2):
        dummy = curr = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        curr.next = list1 or list2
        return dummy.next
        