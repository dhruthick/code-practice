class Solution:
    '''
    MEDIUM: 36
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use hashmap
        from collections import defaultdict
        row_dict, col_dict, box_dict = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = board[i][j]
                    if n in row_dict[i] or n in col_dict[j] or n in box_dict[(i // 3, j // 3)]:
                        return False
                    row_dict[i].add(n)
                    col_dict[j].add(n)
                    box_dict[(i // 3, j // 3)].add(n)
        return True