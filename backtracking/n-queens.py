class Solution:
    '''
    HARD: 51
    The n-queens puzzle is the problem of placing n queens 
    on an n x n chessboard such that no two queens attack each other.

    Given an integer n, return all distinct solutions to the 
    n-queens puzzle. You may return the answer in any order.

    Each solution contains a distinct board configuration of the n-queens' 
    placement, where 'Q' and '.' both indicate a queen and an empty space, 
    respectively.
    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        # to get the answer in the required format
        def get_board(state):
            board = []
            for row in state:
                board.append(''.join(row))
            return board

        # backtracking obviously
        # main problem was figuring out how to validate the two diagonals
        #   - diagonal: row - col value is the same
        #   - anti-diagonal: row + col value is the same
        answers = []
        def backtrack(state, row, o_cols, o_diags, o_antis):
            if row == n:
                # all queens have been placed, arrived at an answer
                answers.append(get_board(state))
                return
            # check every col on this row for safe placement
            for col in range(n):
                # if safe placement is not possible, move on
                if col in o_cols or row - col in o_diags or row + col in o_antis:
                    continue
                # place the queen
                state[row][col] = 'Q'
                # add to sets
                o_cols.add(col)
                o_diags.add(row - col)
                o_antis.add(row + col)
                # go to the next row
                backtrack(state, row + 1, o_cols, o_diags, o_antis)
                # unplace the queen
                state[row][col] = '.'
                # remove from sets
                o_cols.remove(col)
                o_diags.remove(row - col)
                o_antis.remove(row + col)
        
        init_state = [['.'] * n for i in range(n)]
        backtrack(init_state, 0, set(), set(), set())
        return answers