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
        # time - O(n), space - O(1)
        profit = 0
        min_so_far = float('inf')
        for price in prices:
            min_so_far = min(min_so_far, price)
            profit = max(price - min_so_far, profit)
        return profit