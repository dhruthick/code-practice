class Solution:
    '''
    MEDIUM: 53
    Given an integer array nums, find the subarray with 
    the largest sum, and return its sum.
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        # time - O(n), space - O(1)
        # kadane's algorithm
        ans = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            ans = max(ans, max_so_far)
        return ans
        