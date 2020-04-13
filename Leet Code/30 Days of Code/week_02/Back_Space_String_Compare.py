class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        stack1 = []
        stack2 = []
        for i in S:
            if i == "#":
                if len(stack1):
                    stack1.pop()
            else:
                stack1.append(i)
        for j in T:
            if j == "#":
                if len(stack2):
                    stack2.pop()
            else:
                stack2.append(j)
        if stack1 == stack2:
            return 'true'
        else:
            return 'false'

c = Solution()
print(c.backspaceCompare("a#c","b"))