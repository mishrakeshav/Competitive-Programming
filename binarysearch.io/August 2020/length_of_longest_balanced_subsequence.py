class Solution:
    def solve(self, s):
        # Write your code here
        
        stack = []
        count = 0 
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if len(stack):
                    element = stack.pop()
                    count += 2
        
        return count
                
                
