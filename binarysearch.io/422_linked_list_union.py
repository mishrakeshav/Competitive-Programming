# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, ll1, ll2):
        head = LLNode(-1)
        curr = head
        while ll1 and ll2:
            if ll1.val < ll2.val:
                curr.next = LLNode(ll1.val)
                ll1 = ll1.next 
            elif ll1.val > ll2.val:
                curr.next = LLNode(ll2.val)
                ll2 = ll2.next 
            else:
                curr.next = LLNode(ll1.val)
                ll1 = ll1.next 
                ll2 = ll2.next 
            curr = curr.next
        while ll1:
            curr.next = LLNode(ll1.val)
            ll1 = ll1.next 
            curr = curr.next 
        while ll2:
            curr.next = LLNode(ll2.val)
            ll2 = ll2.next 
            curr = curr.next 
        return head.next 