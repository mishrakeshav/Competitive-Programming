# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        # Write your code here
        curr = head
        if curr is None:
            return True 
        elif curr.next is None:
            return True 
        else:
            prev = curr.val
            curr = curr.next
            while curr:
                if curr.val <= prev:
                    return False
                prev = curr.val
                curr = curr.next
        return True
                
                
