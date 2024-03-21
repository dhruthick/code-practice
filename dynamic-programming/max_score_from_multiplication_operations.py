class Solution(object):
    '''
    1770:HARD
    You are given two 0-indexed integer arrays nums and 
    multipliers of size n and m respectively, where n >= m.
    
    You begin with a score of 0. You want to perform 
    exactly m operations. On the ith operation (0-indexed) you will:

        Choose one integer x from either the start or 
        the end of the array nums.

        Add multipliers[i] * x to your score.
        Note that multipliers[0] corresponds to the first operation, 
        multipliers[1] to the second operation, and so on.
        
        Remove x from nums.
    
    Return the maximum score after performing m operations.
    '''
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        m = len(multipliers)
        mem = {}
        def maxScore(left, i):
            if i == m:
                return 0
            right = len(nums) - 1 - (i - left)
            if (left, i) not in mem:
                mem[(left, i)] = max(nums[left] * multipliers[i] \
                    + maxScore(left + 1, i + 1), \
                    nums[right] * multipliers[i] + \
                    maxScore(left, i + 1))
            return mem[(left, i)]
        return maxScore(0, 0)