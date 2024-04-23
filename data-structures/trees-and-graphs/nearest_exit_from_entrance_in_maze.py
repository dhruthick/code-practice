class Solution(object):
    '''
    MEDIUM: 1926
    You are given an m x n matrix maze (0-indexed) with empty cells 
    (represented as '.') and walls (represented as '+'). You are also 
    given the entrance of the maze, where entrance = [entrancerow, entrancecol] 
    denotes the row and column of the cell you are initially standing at.

    In one step, you can move one cell up, down, left, or right. You cannot 
    step into a cell with a wall, and you cannot step outside the maze. Your 
    goal is to find the nearest exit from the entrance. An exit is defined as 
    an empty cell that is at the border of the maze. The entrance does not 
    count as an exit.

    Return the number of steps in the shortest path from the entrance to the 
    nearest exit, or -1 if no such path exists.
    '''
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        q = [(entrance[0], entrance[1], 0)]
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            curr_x, curr_y, dist = q.pop(0)
            for r_off, c_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = curr_x + r_off, curr_y + c_off
                if 0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return dist + 1
                    maze[x][y] = '+'
                    q.append((x, y, dist + 1))
        
        return - 1

