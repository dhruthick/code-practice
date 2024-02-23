class Solution:
    '''
    200: MEDIUM
    Given an m x n 2D binary grid grid which 
    represents a map of '1's (land) and '0's 
    (water), return the number of islands.
    
    An island is surrounded by water and is 
    formed by connecting adjacent lands 
    horizontally or vertically. You may 
    assume all four edges of the grid are 
    all surrounded by water.
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        
        def dfs(row, col):
            grid[row][col] = "X"
            for rOffset, cOffset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                r, c = row + rOffset, col + cOffset
                if 0 <= r < nRows and 0 <= c < nCols and grid[r][c] == "1":
                    dfs(r, c)
            return
        
        num_islands = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)
        return num_islands