class Solution:
    '''
    417: MEDIUM

    There is an m x n rectangular island that borders 
    both the Pacific Ocean and Atlantic Ocean. The 
    Pacific Ocean touches the island's left and top 
    edges, and the Atlantic Ocean touches the 
    island's right and bottom edges.
    
    The island is partitioned into a grid of square 
    cells. You are given an m x n integer matrix 
    heights where heights[r][c] represents the height 
    above sea level of the cell at coordinate (r, c).
    
    The island receives a lot of rain, and the rain 
    water can flow to neighboring cells directly north, 
    south, east, and west if the neighboring cell's 
    height is less than or equal to the current cell's 
    height. Water can flow from any cell adjacent to an 
    ocean into the ocean.
    
    Return a 2D list of grid coordinates result where 
    result[i] = [ri, ci] denotes that rain water can 
    flow from cell (ri, ci) to both the Pacific and 
    Atlantic oceans.
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # intuition: instead of doing dfs/bfs on every cell, 
        # do it only on the edges connected to the ocean

        pacific_cells = []
        atlantic_cells = []
        m, n = len(heights), len(heights[0])

        for row in range(m):
            pacific_cells.append((row, 0))
            atlantic_cells.append((row, n - 1))
        for col in range(1, n):
            pacific_cells.append((0, col))
            atlantic_cells.append((m - 1, col - 1))
        
        def bfs(queue):
            reachable = set()
            while queue:
                row, col = queue.pop(0)
                if (row, col) in reachable:
                    continue
                reachable.add((row, col))
                for r_off, c_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= row + r_off < m and 0 <= col + c_off < n \
                            and heights[row +r_off][col + c_off] >= heights[row][col]:
                        queue.append((row + r_off, col + c_off))
            return reachable
        
        pacific_reachable = bfs(pacific_cells)
        atlantic_reachable = bfs(atlantic_cells)
        return list(atlantic_reachable.intersection(pacific_reachable))