class Solution(object):
    '''
    70: EASY
    You are climbing a staircase. 
    It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?
    '''
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # top-down approach with recursion and hashmap
        def dp(i):
            # base case
            if i <= 2:
                return i
            # caching/memoization
            if i not in memo:
                # recurrence relation
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        memo = {} # for memoization
        return dp(n)

        # # bottom-up approach with for loop and array
        # if n == 1:
        #     return 1
            
        # # An array that represents the answer to the problem for a given state
        # dp = [0] * (n + 1)
        # dp[1] = 1 # Base cases
        # dp[2] = 2 # Base cases
        
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2] # Recurrence relation

        # return dp[n]