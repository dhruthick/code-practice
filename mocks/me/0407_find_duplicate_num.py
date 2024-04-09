class Solution(object):
    '''
    MEDIUM: 287
    Given an array of integers nums containing n + 1 integers where 
    each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses 
    only constant extra space.
    '''
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # binary search approach - count how many numbers are <= mid element

        # # 'low' and 'high' represent the range of values of the target
        # low = 1
        # high = len(nums) - 1
        
        # while low <= high:
        #     cur = (low + high) // 2
        #     count = 0

        #     # Count how many numbers are less than or equal to 'cur'
        #     count = sum(num <= cur for num in nums)
        #     if count > cur:
        #         duplicate = cur
        #         high = cur - 1
        #     else:
        #         low = cur + 1
                
        # return duplicate
        # Find the intersection point of the two runners.

        # cycle detetction - floyd's algorithm

        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare