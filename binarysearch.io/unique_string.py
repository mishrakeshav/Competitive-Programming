class Solution:
    def solve(self, s):
        # Write your code here
        c = dict()
        for i in s:
            if i not in  c:
                c[i] = 1
            else:
                return False
        return True
