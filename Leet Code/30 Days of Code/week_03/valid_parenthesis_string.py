class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                open_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if len(open_stack):
                    open_stack.pop()
                elif len(star_stack):
                    star_stack.pop()
                else:
                    return False
            
        while len(open_stack):
            if len(star_stack):
                if open_stack.pop() > star_stack.pop():
                    return False 
            else:
                return False 
        
        return True
                    
                    
                    
                    
            
            
        