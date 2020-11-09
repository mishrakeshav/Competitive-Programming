# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        UP = 'UP'
        RIGHT = 'RIGHT'
        LEFT = 'LEFT'
        stack = []
        idx = 0 
        stack.append(root)
        while idx < len(moves):
            if moves[idx] == UP:
                stack.pop()
            elif moves[idx] == RIGHT:
                stack.append(stack[-1].right)
            elif moves[idx] == LEFT:
                stack.append(stack[-1].left)
            idx += 1
        return stack[-1].val 