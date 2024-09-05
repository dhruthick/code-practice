'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the 
grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be 
translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:

Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:

Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
{'B', '', 'RTLLBLLB', 'BRB', 'RR', 'TRRB', 'RLB', 'BRR', 'BRTTRBTLBB', 'R', 'BRRR', 'BLB', 'BRTRBLBBRR', 'RTRRRLB'}


'''
grid = [[0,0,s,0,s,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],
        [0,0,s,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],
        [0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],
        [1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]]

def distinctIslands(grid):
    rows, cols = len(grid), len(grid[0])
    res = 0
    paths = []

    def dfs(r, c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
            return False
        grid[r][c] = 0
        nonlocal cur
        if dfs(r+1, c):
            cur+="B"
        if dfs(r, c+1):
            cur+="R"
        if dfs(r-1, c):
            cur+="T"
        if dfs(r, c-1):
            cur+="L"
        return True

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                cur = ""
                dfs(r, c)
                paths.append(cur)
    print(set(paths))
    return len(set(paths))

distinctIslands(grid)

'''
{'B', '', 'RTLLBLLB', 'BRB', 'RR', 'TRRB', 'RLB', 'BRR', 'BRTTRBTLBB', 'R', 'BRRR', 'BLB', 'BRTRBLBBRR', 'RTRRRLB'}
'''
'''
['B', '', 'BRTTRBTLBB', '', 'BLB', 'BRR', 'BRTRBLBBRR', 'R', 'R', 'TRRB', '', 'BRRR', 'BRB', '', 'RTLLBLLB', 'R', '', '', '', 'BRR', 'RLB', '', '', 'RTRRRLB', '', '', 'RR', '', '', '']
'''




