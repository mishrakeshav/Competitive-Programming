# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):
        stack = []
        stack.append(root)
        head = LLNode(-1)
        curr = head 
        while stack:
            new = []
            for node in stack:
                curr.next = LLNode(node.val)
                curr = curr.next 
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            stack = new 
        return head.next 
        