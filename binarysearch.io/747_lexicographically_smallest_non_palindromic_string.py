class Solution:
    def solve(self, s):
        s = list(s)
        n = len(s)
        changed = s[::]
        for i in range(n//2):
            if changed[i] == 'a':
                changed[-i-1] = 'b'
            else:
                changed[i] = 'a'
                break 
        to_change = 'z' 
        pos = -1 
        for i in range(n):
            if s[i] > changed[i]:
                if to_change > changed[i]:
                    pos = i 
                    to_change = changed[i]
                    break 
        s[pos] = changed[pos]
        return ''.join(s)