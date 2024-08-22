class Solution(object):
    '''
    198: MEDIUM
    You are a professional robber planning to 
    rob houses along a street. Each house has 
    a certain amount of money stashed, the 
    only constraint stopping you from robbing 
    each of them is that adjacent houses have 
    security systems connected and it will 
    automatically contact the police if two 
    adjacent houses were broken into on the 
    same night.

    Given an integer array nums representing 
    the amount of money of each house, return 
    the maximum amount of money you can rob 
    tonight without alerting the police.
    '''
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time and space - O(n)
        memo = {}
        # top-down approach
        def dp(i):
            # base case
            if i < 2:
                return max(nums[:i + 1])
            # memoization
            if i not in memo:
                # recurrence relation
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        
        return dp(len(nums) - 1)