class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
        ]
        """
        n = len(matrix)
        m = len(matrix[0])
        rows = [1 for i in range(n)]
        cols = [1 for i in range(m)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = 0 
                    cols[j] = 0 
        
        for i in range(n):
            if rows[i] == 0:
                for j in range(m):
                    matrix[i][j] = 0 
        for i in range(m):
            if cols[i] == 0:
                for j in range(n):
                    matrix[j][i] = 0 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = 1 
        col = 1 
        n = len(matrix)
        m = len(matrix[-1])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        row = 0 
                    if j == 0:
                        col = 0 
                    matrix[i][0] = 0 
                    matrix[0][j] = 0 
        
        for i in range(1,m):
            if matrix[0][i] == 0:
                for j in range(n):
                    matrix[j][i] = 0 
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0 
        if row == 0:
            for j in range(m):
                matrix[0][j] = 0 
        if col == 0:
            for j in range(n):
                matrix[j][0] = 0 
        return matrix 