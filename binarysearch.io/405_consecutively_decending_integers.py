class Solution:
    def solve(self, s):
        def helper(prev,curr,length):
            if len(curr) == 0:
                return True 
            if len(curr) < length - 1:
                return False 
            if len(curr) >= length:
                if int(prev) - int(curr[:length]) == 1:
                    return helper(curr[:length],curr[length:],length)
            if length == 1:
                return False 
            if int(prev) - int(curr[:length-1]) == 1:
                return helper(curr[:length-1], curr[length-1:], length-1)
            return False 
        length = len(s)//2
        if len(s)%2:
            length += 1 
        
        for i in range(1,length+1):
            if helper(s[:i],s[i:],i):
                return True 
        return False 