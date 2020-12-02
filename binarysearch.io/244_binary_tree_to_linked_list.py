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
        head = LLNode(-1)
        curr = head 
        def helper(root,curr):
            if root is None:
                return curr 
            if root.left:
                curr = helper(root.left,curr)
            curr.next = LLNode(root.val)
            curr = curr.next 
            if root.right:
                curr = helper(root.right,curr)
            return curr 
        
        helper(root,head)
        return head.next 
                
        