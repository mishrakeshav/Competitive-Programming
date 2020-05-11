# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        left_nodes = []
        waiting = [root]
        while waiting:
            left_nodes.append(waiting[0].val)
            new_waiting = []
            for node in waiting:
                if node.left:
                    new_waiting.append(node.left)
                if node.right:
                    new_waiting.append(node.right)
                
            waiting = new_waiting
        
        return left_nodes
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def helper(root, currLevel, ans):
            if currLevel > ans[-1][1]:
                ans.append((root.val, currLevel))
            if root.left:
                helper(root.left, currLevel+1, ans)
            if root.right:
                helper(root.right, currLevel+1, ans)
            
            
        ans = [(0, -1)]
        helper(root, 0, ans)
        temp = []
        for i in ans[1:]:
            temp.append(i[0])
        return temp