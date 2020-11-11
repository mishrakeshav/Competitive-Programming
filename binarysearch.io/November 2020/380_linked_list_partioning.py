# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        smaller = LLNode(-1)
        equal = LLNode(-1)
        greater = LLNode(-1)
        s = smaller 
        e = equal 
        g = greater
        curr = node
        while curr:
            if curr.val < k:
                s.next = curr 
                s = s.next 
            elif curr.val > k:
                g.next = curr 
                g = g.next
            else:
                e.next = curr 
                e = e.next 
            curr = curr.next 
            e.next = None 
            g.next = None 
            s.next = None 
        s.next = equal.next
        e.next = greater.next 
        return smaller.next 
        
        
        