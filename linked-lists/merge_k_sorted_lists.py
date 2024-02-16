# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    '''
    23: HARD
    You are given an array of k linked-lists lists,
    each linked-list is sorted in ascending order.
    
    Merge all the linked-lists into one sorted 
    linked-list and return it.
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Use the solution for merging two lists
        # # def mergeTwoLists(list1, list2):
        # #     dummy = curr = ListNode()
            
        # #     while list1 and list2:
        # #         if list1.val < list2.val:
        # #             curr.next = list1
        # #             list1 = list1.next
        # #         else:
        # #             curr.next = list2
        # #             list2 = list2.next
        # #         curr = curr.next
                
        # #     curr.next = list1 or list2
        # #     return dummy.next
        # # if len(lists) == 1:
        # #     return lists[0]
        # # elif len(lists) == 0:
        # #     return None
        # # answer = mergeTwoLists(lists[0], lists[1])
        # # for i in range(2, len(lists)):
        # #     answer = mergeTwoLists(answer, lists[i])
        # # return answer

        # faster approach, brute force with code optimization.
        def get_val(elem):
            return elem.val

        arr = []
        for list in lists:
            elem = list
            while elem:
                arr.append(elem)
                elem = elem.next
        
        arr.sort(key=get_val)

        if not arr: return None
        for i in range(len(arr) - 1):
            arr[i].next = arr[i+1]
        arr[-1].next = None
        return arr[0]
        
        