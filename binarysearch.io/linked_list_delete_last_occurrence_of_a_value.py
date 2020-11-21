"""
Problem Link: https://binarysearch.io/problems/Linked-list-delete-last-occurrence-of-value
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        # Write your code here
        latest = None 
        latest_prev = None 
        prev = None 
        if node.val == target:
            prev = None 
            latest = node 
        
        current = node 
        while current:
            if current.val == target:
                latest_prev = prev 
                latest = current 
            
            prev = current 
            current = current.next 
        
        if latest_prev:
            latest_prev.next = latest.next 
            return node 
        elif node.val == target:
            node = node.next 
            return node 
        else:
            return node
            


