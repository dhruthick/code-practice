class Solution:
    '''
    MEDIUM: 48
    You are given an n x n 2D matrix representing an image, 
    rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you 
    have to modify the input 2D matrix directly. DO NOT 
    allocate another 2D matrix and do the rotation.
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = (
                    matrix[i][-j - 1],
                    matrix[i][j],
                )