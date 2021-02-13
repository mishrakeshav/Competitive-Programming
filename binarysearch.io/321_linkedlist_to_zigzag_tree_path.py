# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        tree = Tree(-float('inf'))
        itr = tree
        curr = node 
        while curr:
            val = curr.val 
            if val >= itr.val :
                itr.right = Tree(val)
                itr = itr.right 
            else:
                itr.left = Tree(val)
                itr = itr.left 
            curr = curr.next 

        return tree.right  