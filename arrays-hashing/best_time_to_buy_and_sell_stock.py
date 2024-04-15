class Solution:
    '''
    EASY: 121
    You are given an array prices where prices[i] is the price 
    of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to 
    buy one stock and choosing a different day in the future to 
    sell that stock.

    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l]>=prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r]-prices[l])
            r+=1
        
        return max_profit