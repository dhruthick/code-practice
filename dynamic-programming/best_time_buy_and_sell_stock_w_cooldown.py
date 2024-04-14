class Solution:
    '''
    MEDIUM: 309
    You are given an array prices where prices[i] is the price of a given 
    stock on the ith day.

    Find the maximum profit you can achieve. You may complete as many 
    transactions as you like (i.e., buy one and sell one share of the 
    stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day 
    (i.e., cooldown one day).
    
    Note: You may not engage in multiple transactions simultaneously 
    (i.e., you must sell the stock before you buy again).
    '''
    def maxProfit(self, prices: List[int]) -> int:
        # cache makes a big difference!
        @lru_cache(None)
        def dp(i, in_cooldown, holding):
            if i == len(prices):
                return 0
            doNothing = dp(i + 1, 0, holding)
            if holding:
                # best of sell or don't sell
                return max(prices[i] + dp(i + 1, 1, 0), doNothing)
            if in_cooldown:
                # do nothing is the only choice
                return doNothing
            # best of buy or don't buy
            return max(- prices[i] + dp(i + 1, 0, 1), doNothing)
        return dp(0, 0, 0)