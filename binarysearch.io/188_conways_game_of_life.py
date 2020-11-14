class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[-1])
        dy = [1, 0, -1, 0  ,-1, -1 ,1,1]
        dx = [0, 1, 0 , -1, -1, 1 , -1,1]
        ans = []
        for i in range(n):
            ans.append([])
            for j in range(m):
                b = 0 
                for k in range(8):
                    y = i + dy[k] 
                    x = j + dx[k]
                    if 0 <= y < n and 0 <= x < m:
                        b += matrix[y][x]
                if matrix[i][j] == 0 and b == 3:
                    ans[-1].append(1)
                elif matrix[i][j] == 1 and 2 <= b <= 3:
                    ans[-1].append(1)
                else:
                    ans[-1].append(0)
        return ans