class Solution(object):
    '''
    MEDIUM: 695
    You are given an m x n binary matrix grid. An island is a group of 1's 
    (representing land) connected 4-directionally (horizontal or vertical.) 
    You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.
    '''
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.visited = set()
        self.m = len(grid)
        self.n = len(grid[0])

        def bfs(i, j):
            area = 1
            self.visited.add((i, j))
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                for r_of, c_of in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                    if 0 <= x + r_of < self.m and 0 <= y + c_of < self.n and grid[x + r_of][y + c_of] == 1:
                        if (x + r_of, y + c_of) not in self.visited:
                            # print((x + r_of, y + c_of))
                            area += 1
                            self.visited.add((x + r_of, y + c_of))
                            q.append((x + r_of, y + c_of))
            return area
        
        max_area = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    # print((i,j))
                    max_area = max(max_area, bfs(i, j))
                    # print(" ")
        return max_area