# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        # Write your code here
        
        if k == 0:
            curr = node 
            while curr.next:
                curr = curr.next 
            return curr.val 
        
        count = k
        curr = node 
        acc = None 
        
        while curr.next:
            count -= 1
            curr = curr.next 
            if count == 0:
                acc = node 
            elif count < 0:
                acc = acc.next 
        return acc.val 
class Solution:
    def solve(self, head, k):
        front, back = head, head
        for _ in range(k + 1):
            back = back.next
        
        while back:
            front, back = front.next, back.next
            
        return front.val
        
                
            
            
            
            
                
                
        
        
        
            
