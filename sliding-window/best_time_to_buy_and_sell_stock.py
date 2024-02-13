class Solution(object):
    '''
    121: EASY
    You are given an array prices where prices[i]
    is the price of a given stock on the ith day.
    
    You want to maximize your profit by choosing a 
    single day to buy one stock and choosing a 
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from 
    this transaction. If you cannot achieve any 
    profit, return 0.
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # set first price to minimum
        minp = prices[0]
        profit = 0
        for p in prices:
            # change minimum when the price is lower
            if minp > p:
                minp = p
            # otherwise compute profit and update max
            elif minp < p:
                profit = max(profit, p - minp)
        return profit