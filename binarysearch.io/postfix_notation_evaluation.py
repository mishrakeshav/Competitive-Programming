class Solution:
    def solve(self, exp):
        # Write your code here
        stack = []
        for i in exp:
            # print(stack)
            if i in "+/*-":
                a = stack.pop()
                b = stack.pop()
                c = int(eval(b + i + a))
                stack.append(str(c))
            else:
                stack.append(i)
        return int(stack[0])
            
