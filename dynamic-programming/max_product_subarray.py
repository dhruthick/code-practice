class Solution:
    '''
    MEDIUM: 152
    Given an integer array nums, find a subarray that has the largest product, 
    and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums.copy()
        mn = nums.copy()

        for i in range(1, len(nums)):
            mx[i] = max(nums[i], nums[i] * mx[i-1], nums[i] * mn[i-1])
            mn[i] = min(nums[i], nums[i] * mx[i-1], nums[i] * mn[i-1])
        
        return max(mx)
        