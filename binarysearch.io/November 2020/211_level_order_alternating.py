# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def solve(self, root):
        s = 0
        q = []
        q.append(root)
        ans = [root.val,]
        while len(q):
            new = []
            for node in q:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if s%2:
                ans.extend([node.val for node in new])
            else:
                ans.extend([node.val for node in reversed(new)])
            q = new
            s += 1
        return ans