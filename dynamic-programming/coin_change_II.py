class Solution:
    '''
    MEDIUM: 518
    You are given an integer array coins representing coins of different 
    denominations and an integer amount representing a total amount of 
    money.

    Return the number of combinations that make up that amount. If that 
    amount of money cannot be made up by any combination of the coins, 
    return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @lru_cache(None)
        # number of ways to make amount with n - i coins
        def dp(amt, i):
            if amt == 0:
                return 1
            if i == n:
                return 0
            if coins[i] > amt:
                return dp(amt, i + 1)
            # either pick the coin or don't pick the coin
            return dp(amt - coins[i], i) + dp(amt, i + 1)
        
        return dp(amount, 0)