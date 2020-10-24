class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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

[
    [1,2,3,4],
    [5,0,7,8],
    [0,10,11,12],
    [13,14,15,0]
]