# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):

        s1 = ""
        s2  = ""
        curr1 = l0 
        curr2 = l1 
        while curr1:
            s1 += str(curr1.val) 
            curr1 = curr1.next 
        print(s1)
        
        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next 
        print(s2)
        head = LLNode(-1)
        curr = head 
        s = str(int(s1[::-1]) + int(s2[::-1]))
        for i in reversed(s):
            curr.next = LLNode(int(i))
            curr = curr.next 
        return head.next 


        