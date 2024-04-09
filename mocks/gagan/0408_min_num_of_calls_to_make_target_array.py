class Solution:
    '''
    MEDIUM: 1558
    You are given an integer array nums. You have an integer array arr of the same length with all 
    values set to 0 initially. You also have the following modify function:
        Two operations:
        1. increment element at any one index by 1
        2. double all the elements

    You want to use the modify function to convert arr to nums using the minimum number of calls.

    Return the minimum number of function calls to make nums from arr.

    The test cases are generated so that the answer fits in a 32-bit signed integer.
    '''
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while any(nums):
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
            if any(nums):
                for i in range(len(nums)):
                    nums[i] //= 2
                count += 1
        return count