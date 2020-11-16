# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l1, l2):
        n1 = 0
        curr1 = l1 
        curr2 = l2
        head = LLNode(-1)
        curr = head 
        while curr1 and curr2:
            if curr1.val == curr2.val:
                curr.next = LLNode(curr1.val)
                curr = curr.next 
                curr1 = curr1.next 
                curr2 = curr2.next 
            elif curr1.val < curr2.val:
                curr1 = curr1.next 
            else:
                curr2 = curr2.next 
        return head.next 