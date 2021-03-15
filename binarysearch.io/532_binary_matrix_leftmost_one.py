class Solution:
    def solve(self, matrix):
        if not matrix:
            return -1
        i = 0 
        j = len(matrix[-1]) - 1  
        mi = -1
        while i < len(matrix) and j >= 0:
            if matrix[i][j]:
                mi = j 
                j -= 1 
            else:
                i += 1 
        return mi