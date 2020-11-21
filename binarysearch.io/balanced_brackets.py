class Solution:
    def solve(self, s):
        # Write your code here
        stack = []
        
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if len(stack):
                    if stack.pop() == "(":
                        pass 
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
