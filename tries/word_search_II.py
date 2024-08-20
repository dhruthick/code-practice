class Solution:
    '''
    212: HARD
    Given an m x n board of characters and a 
    list of strings words, return all words on 
    the board.
    
    Each word must be constructed from letters 
    of sequentially adjacent cells, where 
    adjacent cells are horizontally or 
    vertically neighboring. The same letter 
    cell may not be used more than once in 
    a word.
    '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # M - number of cells on the board
        # L - maximum length of a word
        # N - number of non overlapping letters in all words (size of trie)
        # time - O(M * 4 * 3^(L - 1))
        # space - O(N) 


        # build trie for the given words
        word_key = '#'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[word_key] = word
            
        def backtrack_search(x, y, node):
            letter = board[x][y]
            # check if there is a word at this cell at this point
            cur = node[letter]
            word = cur.pop(word_key, False)
            if word:
                res.append(word)
            # mark cell as visited
            board[x][y] = '*'
            for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + r, y + c
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in cur:
                    backtrack_search(nx, ny, cur)
            board[x][y] = letter
            
            # For a leaf node in Trie, once we traverse it 
            # (i.e. find a matched word), we would no longer 
            # need to traverse it again
            if not cur:
                node.pop(letter)

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack_search(i, j, trie)

        return res