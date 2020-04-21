# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        curr = node 
        next = None
        prev = None
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr 
            curr = next 
        return prev
            
