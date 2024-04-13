class Solution(object):
    '''
    MEDIUM: 221
    Given an m x n binary matrix filled with 0's and 1's, find the 
    largest square containing only 1's and return its area.

    '''
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        # dp array with extra row and column of zeroes above and left side
        # dp[i][j] = size of max square possible in a square with bottom
        # right index at i, j.

        # ALWAYS USE LIST COMPREHENSION TO INITIALIZE MULTIDIMENSIONAL ARRAYS
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        # bottom up approach
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if its 1, check minimum of squares at top, left, and top-left
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len
