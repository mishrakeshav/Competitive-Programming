class Solution:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transpose 
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # swap columns
        for i in range(n):
            for j in range(1,n//2+1):
                matrix[i][j-1],matrix[i][-j] = matrix[i][-j],matrix[i][j-1]
        