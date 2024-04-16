class Solution:
    '''
    MEDIUM: 276
    You are painting a fence of n posts with k different colors. 
    You must paint the posts following these rules:

    Every post must be painted exactly one color.
    There cannot be three or more consecutive posts with the same color.

    Given the two integers n and k, return the number of ways you can paint the fence.
    '''
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(None)
        # number of ways to paint i posts
        def dp(i):
            # number of ways to paint 1 post
            if i == 1:
                return k
            # number of ways to paint 2 posts
            if i == 2:
                return k * k
            # number of ways to paint i posts = 
            # number of ways to paint a different color from (i - 1)th post +
            # number of ways to paint the same color as (i - 1)th post.

            # number of ways to paint a different color from (i - 1)th post = 
            # (k - 1) * dp(i - 1)

            # number of ways to paint the same color as (i - 1)th post =
            # 1 * number of ways to paint (i - 1)th post different from (i - 2)th post =
            # 1 * (k - 1) * dp(i - 2)
            
            # number of ways to paint i posts = 
            # (k - 1) * (dp(i - 1) + dp(i - 2))
            return (k - 1) * (dp(i - 1) + dp(i - 2))
            
        return dp(n)