class Solution:
    '''
    79: MEDIUM

    Given an m x n grid of characters board and a string 
    word, return true if word exists in the grid.
    
    The word can be constructed from letters of 
    sequentially adjacent cells, where adjacent cells 
    are horizontally or vertically neighboring. The same 
    letter cell may not be used more than once.
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        # l - length of word
        # n - dimension of board
        # time - O(n * 3^l)
        # space - O(l)
        row_length, col_length = len(board), len(board[0])

        
        def find_word(row, col, letters_left):

            if len(letters_left) == 0:
                return True

            if row < 0 or row == row_length or col < 0 or col == col_length \
                    or board[row][col] != letters_left[0]:
                return False
            # use the board itself to track instead of extra space
            board[row][col] = '*'
            for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if find_word(row + r_offset, col + c_offset, letters_left[1:]):
                    return True
            board[row][col] = letters_left[0]

            return False
        

        for row in range(row_length):
            for col in range(col_length):
                if find_word(row, col, word):
                    return True
        return False