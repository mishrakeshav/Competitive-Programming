class Solution:
    def solve(self, s, words):
        # Write your code here
        new = []
        for i in words:
            if i.startswith(s):
                new.append(i)
        return new
