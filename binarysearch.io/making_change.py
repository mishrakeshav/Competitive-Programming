class Solution:
    def solve(self, n):
        # Write your code here
        count = 0
        if n >= 25:
            count += n // 25
            n %= 25
        if n >= 10:
            count += n // 10
            n %= 10
        if n >= 5:
            count += n // 5
            n %= 5
        count += n

        return count
