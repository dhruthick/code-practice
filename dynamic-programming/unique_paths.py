class Solution:
    '''
    MEDIUM: 62
    There is a robot on an m x n grid. The robot is initially located at the 
    top-left corner (i.e., grid[0][0]). The robot tries to move to the 
    bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only 
    move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths 
    that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or 
    equal to 2 * 109.
    '''
    # time and space - O(mn)
    @lru_cache(None)
    def backtrack(self, i, j):
        if i == self.m - 1 and j == self.n - 1:
            return 1
        num_ways = 0
        for x, y in [(0, 1), (1, 0)]:
            nx, ny = i + x, j + y
            if 0 <= nx < self.m and 0 <= ny < self.n:
                num_ways += self.backtrack(nx, ny)
        return num_ways
    
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n

        return self.backtrack(0, 0)