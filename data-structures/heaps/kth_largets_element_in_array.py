class Solution(object):
    '''
    Given an integer array nums and an integer k, 
    return the kth largest element in the array.

    Note that it is the kth largest element in the 
    sorted order, not the kth distinct element.

    Can you solve it without sorting?
    '''
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        size = 0
        for num in nums:
            heapq.heappush(heap, num)
            size += 1
            if size > k:
                heapq.heappop(heap)
                size -= 1
        
        return heap[0]

        # # alternate approach, which is better?
        # from heapq import heappop, heapify
        # nums = [-x for x in nums]
        # heapify(nums)
        # answer = None
        # while k:
        #     answer = -heappop(nums)
        #     k -= 1
        # return answer