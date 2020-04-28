class Solution:
    def solve(self, matrix):
        # Write your code here
        n = len(matrix)
        m = len(matrix[0])
        col = [False for i in range(m)]
        row = [False for i in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    col[j] = True
                    row[i] = True
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        return matrix
