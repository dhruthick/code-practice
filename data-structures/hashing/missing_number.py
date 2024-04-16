class Solution:
    '''
    EASY: 268
    Given an array nums containing n distinct numbers in 
    the range [0, n], return the only number in the range 
    that is missing from the array.
    '''
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        og_sum = int(n * (n + 1) / 2)
        given_sum = sum(nums) 

        return og_sum - given_sum