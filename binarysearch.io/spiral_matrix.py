class Solution:
    def solve(self, matrix):
        # Write your code here
        n1 = 0
        m1 = 0
        n2 = len(matrix) - 1
        m2 = len(matrix[0]) - 1
        n = len(matrix) - 1
        m = len(matrix[0]) - 1
        l = []

        while n1 < n2 and m1 < m2:
            for i in range(m1, m2 + 1):
                l.append(matrix[n1][i])

            for i in range(n1 + 1, n2 + 1):
                l.append(matrix[i][m2])

            for i in range(m2 - 1, m1 - 1, -1):
                l.append(matrix[n2][i])

            for i in range(n2 - 1, n1 + 1, -1):
                l.append(matrix[i][m1])

        n1 += 1
        n2 -= 1
        m1 += 1
        m2 -= 1

        if n == m:
            l.append(matrix[n1][m1])
            return l

        if m % 2:
            for i in range(n1, n2 + 1):
                l.append(matrix[i][m1])
            return l

        if n % 2:
            for i in range(m1, m2 + 1):
                l.append(matrix[n1][i])

        return l
