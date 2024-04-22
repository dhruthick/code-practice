class KthLargest(object):
    '''
    EASY: 703
    Design a class to find the kth largest element in a stream. 
    Note that it is the kth largest element in the sorted order, 
    not the kth distinct element.

    Implement KthLargest class:

    - KthLargest(int k, int[] nums) Initializes the object with 
    the integer k and the stream of integers nums.
    - int add(int val) Appends the integer val to the stream and 
    returns the element representing the kth largest element in 
    the stream.
    '''
    from heapq import heapify, heappop, heappush
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        self.size = 0
        for num in nums:
            heappush(self.heap, num)
            self.size += 1
            if self.size > k:
                heappop(self.heap)
                self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.heap, val)
        self.size += 1
        if self.size > self.k:
            heappop(self.heap)
            self.size -= 1
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)