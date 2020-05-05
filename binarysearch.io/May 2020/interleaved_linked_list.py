# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
"""
Given two linked lists l0 and l1, return the two linked lists interleaved, 
starting with l0. 
If there are leftover nodes in a linked list, they should be added to the end.
Example:
l0 = 7 → 8 → 9
l1 = 1 → 2
7 → 1 → 8 → 2 → 9
"""
class Solution:
    def solve(self, l0, l1):
        head = None
        curr = None
        curr1 = l0
        curr2 = l1
        l0 = l0.next
        l1 = l1.next
        while curr1 and curr2:
            curr1.next = curr2
            if not head:
                head = curr1
                curr = head.next
            else:
                curr.next = curr1
                curr = curr2
            curr1 = l0
            curr2 = l1
            if l0:
                l0 = l0.next
            if l1:
                l1 = l1.next
                
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        return head