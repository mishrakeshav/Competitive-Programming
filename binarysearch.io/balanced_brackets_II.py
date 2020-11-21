class Solution:
    def solve(self, s):
        # Write your code here
        stack = []
        string_open = ["(", "[", "{" ]
        string_closed = [")", "]", "}"]
        for i in s:
            if i in string_open:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if string_closed.index(i) != string_open.index(stack.pop()):
                    return False 
        
        return len(stack) == 0
            
            
                    
