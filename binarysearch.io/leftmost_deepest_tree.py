# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def deepest(root,count=0):
            
            if root.left is None and root.right is None:
                return (count,root.val)
            else:
                count += 1
                if root.left is None:
                    right = deepest(root.right,count)
                    return right
                elif root.right is None:
                    left = deepest(root.left,count)
                    return left
                
                left = deepest(root.left,count)
                right = deepest(root.right,count)
                if left[0] >= right[0]:
                    return left
                else:
                    return right
        return deepest(root)[1]

class Solution:
    def solve(self, root):
        nodeLevel = {}
        waiting = [root]
        while(waiting):
            newWaiting = []
            for node in waiting:
                if node.left:
                    newWaiting.append(node.left)
                if node.right:
                    newWaiting.append(node.right)
            if newWaiting == []:
                return waiting[0].val
            waiting = newWaiting    
                    
