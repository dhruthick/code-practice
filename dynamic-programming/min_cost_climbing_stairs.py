class Solution(object):
    '''
    746: EASY

    You are given an integer array cost where 
    cost[i] is the cost of ith step on a 
    staircase. Once you pay the cost, you can 
    either climb one or two steps.

    You can either start from the step with 
    index 0, or the step with index 1.

    Return the minimum cost to reach the top 
    of the floor.
    '''
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        memo = {}
        cost.append(0)
        def dp(i):
            if i < 2:
                return cost[i]
            if i not in memo:
                memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
            return memo[i]
        
        return dp(len(cost) - 1)