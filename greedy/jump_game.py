class Solution:
    '''
    MEDIUM: 55
    You are given an integer array nums. You are initially positioned at 
    the array's first index, and each element in the array represents 
    your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
    '''
    def canJump(self, nums: List[int]) -> bool:
        # time - O(n), space - O(1)
        g = len(nums) - 1
        # start from the end
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= g:
                g = i
        
        return True if g == 0 else False