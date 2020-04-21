# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def solve(self, node):
        A, B = split_list_by_half(node)
        B = reverse(B)
        return all(a == b for a, b in zip(it(A), it(B)))
            
def split_list_by_half(head):
    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next
    if prev:
        prev.next = None
    return head, slow
    
def reverse(head):
    queue = deque((None, head))
    while queue[-1]:
        node = queue[-1]
        queue.append(node.next)
        node.next = queue.popleft()
    return queue[0]
    
def it(head):
    while head:
        yield head.val
        head = head.next
class Solution:
    def solve(self, node):
        # Write your code here
        curr = node 
        curr2 = node
        l = []
        while True:
            if curr2.next is None:
                curr = curr.next 
                i = -1
                
                while curr:
                    if curr.val != l[i]:
                        return False
                    curr = curr.next 
                    i -= 1
                else:
                    return True
            elif curr2.next.next is None:
                i = -1
                while curr:
                    if curr.val != l[i]:
                        return False
                    curr = curr.next 
                    i -= 1
                else:
                    return True
            else:
                l.append(curr.val)
                curr = curr.next 
                curr2 = curr2.next.next
                
                
                
                
                
        
        
