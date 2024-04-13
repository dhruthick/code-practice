class Solution:
    '''
    MEDIUM: 322
    You are given an integer array coins representing coins of 
    different denominations and an integer amount representing a 
    total amount of money.

    Return the fewest number of coins that you need to make up 
    that amount. If that amount of money cannot be made up by 
    any combination of the coins, return -1.

    You may assume that you have an infinite number of each 
    kind of coin.
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def min_denom(amt):
            # base cases
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            # iterable recurrence relation
            best = float('inf')
            for coin in coins:
                next_min = min_denom(amt - coin)
                if next_min != -1:
                    best = min(next_min + 1, best)
            return best if best != float('inf') else -1
            
        return min_denom(amount)

        

        