# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, i, j):
        head = node 
        start_prev = None 
        start = node 
        for i in range(i):
            start_prev = start 
            start = start.next 
        end = node 
        end_next = None 
        for i in range(j):
            end = end.next 
            end_next = end.next
        print(start.val,end.val)
        if start_prev:
            start_prev.next = end
        else:
            head = end 
        prev = None 
        curr = start 

        while curr is not end:
            print(curr.val)
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        end.next = prev 
            
        start.next = end_next  
        return head
 
        