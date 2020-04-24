# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        # Write your code here
        n = 0
        curr = node
        while curr:
            curr = curr.next
            n += 1
        
        if k%n==0:
            return node
        if k>n:
            k = k%n
        curr = node
        k1 = n-k-1
        while k1!=0:
            curr = curr.next
            k1 -= 1
        replace = curr
        head = curr.next
        while curr.next:
            curr = curr.next 
        curr.next = node
        replace.next = None
        return head
        
            
            
        
            
        
