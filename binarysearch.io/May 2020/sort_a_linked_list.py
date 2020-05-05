# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
"""
Given a singly linked list of integers,
sort the nodes by their values in ascending order.
"""

class Solution:
    def solve(self, node):
        # Write your code here
        l = []
        curr = node
        while curr:
            l.append(curr.val)
            curr=curr.next 
        
        l.sort()
        curr = node
        i = 0
        while curr:
            curr.val = l[i]
            i += 1
            curr = curr.next
        
        return node
            
        
        
        
