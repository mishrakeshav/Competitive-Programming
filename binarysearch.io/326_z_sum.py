class Solution:
    def solve(self, matrix):
        n = len(matrix)
        ans = 0 
        if n == 1 :
            return matrix[-1][-1]
        for i in range(n):
            ans += matrix[0][i]
            ans += matrix[-1][i]
        
        for i in range(1,n-1):
            ans += matrix[i][-i - 1]
        return ans