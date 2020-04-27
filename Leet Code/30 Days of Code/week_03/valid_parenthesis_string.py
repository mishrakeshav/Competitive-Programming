"""
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity of a string by these rules:

1.Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2.Any right parenthesis ')' must have a corresponding left parenthesis '('.
3.Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4.'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5.An empty string is also valid.
"""

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
                    
                    
                    
                    
            
            
        