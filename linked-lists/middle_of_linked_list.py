class Solution(object):
    '''
    876: EASY
    Given the head of a singly linked list, return the
    middle node of the linked list. 
    If there are two middle nodes, return the
    second middle node.
    '''
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        mid = (length + 2) // 2 - 1
        curr = head
        while mid:
            mid -= 1
            curr = curr.next
        return curr