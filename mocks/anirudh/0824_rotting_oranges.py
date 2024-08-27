'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a
 fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraint:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

'''
import collections
def orangesRotting(grid) -> int:
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    #Get coordinates of the rotten, count the number of fresh oranges
    fresh, rotten = 0, collections.deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r, c))
            elif grid[r][c] == 1:
                fresh+=1
    time = 0
    #print("Number of fresh oranges {}, rotten {}".format(fresh, rotten))
    while rotten and fresh: 
        time+=1
        size = len(rotten)
        for i in range(size):
            x, y = rotten.popleft()
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                next_x, next_y = x+dx, y+dy
                if next_x < 0 or next_y < 0 or next_x>=rows or next_y>=cols:
                    continue

                if grid[next_x][next_y] == 0 or grid[next_x][next_y]==2:
                    continue
                
                grid[next_x][next_y] = 2
                fresh-=1
                rotten.append((next_x, next_y))

    return time if fresh == 0 else -1

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
assert orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert orangesRotting([[0,2]]) == 0

# time = 0
# [[2,1,1],
#  [1,1,0],
#  [0,1,1]]

#  time= 1
# [[2,2,1],
#  [2,1,0],
#  [0,1,1]]
#  time =2 
#  [[2,2,2],
#  [2,2,0],
#  [0,2,2]]
