# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
"""
Given a singly linked list node, return the value of the middle node.
If there's two middle nodes, then return the second one.
Examples:

Given 5 -> 2 -> 3, return 2.

Given 4 -> 0 -> 3 -> 9, return 3.

Bonus: Can you do this in one pass?
"""

class Solution:
    def solve(self, node):
        # Write your code here
        fast = node
        slow = node

        while fast.next:
            if fast.next.next is None:
                return slow.next.val
            fast = fast.next.next
            slow = slow.next
        return slow.val
