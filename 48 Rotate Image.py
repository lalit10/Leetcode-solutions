class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Use maths
        #1. Transpose on diagonal
        #2. Reverse in row

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #print("Matrix is:", matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]

        #print("Matrix is:", matrix)

