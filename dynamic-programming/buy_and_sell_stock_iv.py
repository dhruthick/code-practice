class Solution:
    '''
    HARD: 188
    You are given an integer array prices where prices[i] is the price of 
    a given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at 
    most k transactions: i.e. you may buy at most k times and sell 
    at most k times.

    Note: You may not engage in multiple transactions simultaneously 
    (i.e., you must sell the stock before you buy again).
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        # state variables: day, transactions remaining, indicator (holding stock or not)
        def dp(i, rem_tranc, holding):
            if not rem_tranc:
                return 0
            if i == len(prices):
                return 0
            do_nothing = dp(i + 1, rem_tranc, holding)
            if holding:
                # choose best among selling or not selling
                return max(do_nothing, prices[i] + dp(i + 1, rem_tranc - 1, 0))
            # choose best among buying or not buying
            return max(do_nothing, - prices[i] + dp(i + 1, rem_tranc, 1))
            
        return dp(0, k, 0)