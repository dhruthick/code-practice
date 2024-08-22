class Solution:
    '''
    MEDIUM: 152
    Given an integer array nums, find a subarray that has the largest product, 
    and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.
    '''
    def maxProduct(self, nums: List[int]) -> int:
        # time - O(n), space - O(1)
        max_so_far = nums[0]
        min_so_far = nums[0]
        answer = max_so_far
        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            max_so_far = temp_max
            answer = max(answer, max_so_far)
        return answer
        