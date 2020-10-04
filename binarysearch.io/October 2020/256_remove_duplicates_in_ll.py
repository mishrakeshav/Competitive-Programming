# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        duplicates = set()
        head = node 
        prev = None 
        while head:
            if head.val in duplicates:
                prev.next = head.next
            else:
                prev = head 
            duplicates.add(head.val)
            head = head.next
        
        return node 
        
        
