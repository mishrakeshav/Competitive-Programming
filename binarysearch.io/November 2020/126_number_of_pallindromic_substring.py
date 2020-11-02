class Solution:
    def solve(self, s):
        def expand(i, j):
            ans = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                ans += 1
            return ans

        return sum(expand(i, i) + expand(i, i + 1) for i in range(len(s)))
