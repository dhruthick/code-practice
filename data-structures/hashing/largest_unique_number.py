class Solution:
    '''
    EASY: 1133
    Given an integer array nums, return the largest integer that 
    only occurs once. If no integer occurs once, return -1.
    '''
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import defaultdict

        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        ans = -1
        for num, c in count.items():
            if c == 1 and num > ans:
                ans = num
        return ans