class Solution:
    def solve(self, lst0, lst1):
        # Write your code here
        lst = []
        n = len(lst0) + len(lst1)
        n1 = len(lst0)-1
        n2 = len(lst1)-1
        i = 0
        j = 0
        while i <= n1 and j <= n2:
            if lst0[i] < lst1[j]:
                lst.append(lst0[i])
                i += 1 
            elif lst1[j] < lst0[i]:
                lst.append(lst1[j])
                j += 1 
            else:
                lst.extend([lst0[i], lst1[j]])
                i += 1 
                j += 1 
                
        if i > n1:
            while j <= n2:
                lst.append(lst1[j])
                j += 1 
        elif j > n2:
            while i <= n1:
                lst.append(lst0[i])
                i += 1 
        return lst
                
            