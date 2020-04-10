# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowiter = head
        fastiter = head
        
        while fastiter!=None and fastiter.next!=None:
            fastiter = fastiter.next.next
            slowiter = slowiter.next 
        return slowiter
        