class Solution:
    def solve(self, a, b, target):
        def inorder(l,a):
            if a is None:
                return 
            inorder(l,a.left)
            l.append(a.val)
            inorder(l,a.right)
        
        l = []
        r = []
        inorder(l,a)
        inorder(r,b)
        i = 0 
        j = len(r)-1

        while i < len(l) and j >= 0:
            if l[i] + r[j] == target:
                return True 
            elif l[i] + r[j] < target:
                i += 1 
            else:
                j -= 1 
        return False  