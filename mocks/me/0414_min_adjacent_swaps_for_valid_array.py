class Solution:
    '''
    MEDIUM: 2340
    You are given a 0-indexed integer array nums.

    Swaps of adjacent elements are able to be performed on nums.

    A valid array meets the following conditions:

        - The largest element (any of the largest elements if there are multiple) 
        is at the rightmost position in the array.
        - The smallest element (any of the smallest elements if there are multiple) 
        is at the leftmost position in the array.
        
    Return the minimum swaps required to make nums a valid array.
    '''
    def minimumSwaps(self, nums: List[int]) -> int:
        max_index, min_index = 0, 0
        for i in range(len(nums)):
            if nums[i] >= nums[max_index]:
                max_index = i
            if nums[i] < nums[min_index]:
                min_index = i
        ans = 0
        if max_index < min_index:
            ans = min_index + len(nums) - max_index - 2
        if max_index > min_index:
            ans = min_index + len(nums) - max_index - 1
        # print(ans, min_index, max_index) 
        return ans