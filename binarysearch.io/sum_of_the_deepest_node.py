# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        nodeLevel = {}
        def deepest(root,level=0):
            if root is None:
                return
            else:
                if level not in nodeLevel:
                    nodeLevel[level] = []
                nodeLevel[level].append(root.val)
                deepest(root.left,level+1)
                deepest(root.right, level+1)
        
        deepest(root,0)
        return sum(nodeLevel[max(nodeLevel)])
class Solution:
    def solve(self, root):
        waiting = [root]
        while(waiting):
            newWaiting = []
            possAns = 0
            for node in waiting:
                possAns += node.val
                if node.left:
                    newWaiting.append(node.left)
                    
                if node.right:
                    newWaiting.append(node.right)
            if not newWaiting:
                return possAns
            else:
                waiting = newWaiting
                    
                
            
            
                    
                
            
        
