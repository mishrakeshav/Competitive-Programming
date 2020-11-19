class Solution:
    def solve(self, s, t):
        from collections import Counter
        a_ = Counter(s)
        b_ = Counter(t)
        a = [[i,j] for i,j in a_.items()]
        b = [[i,j] for i,j in b_.items()]
        a.sort()
        b.sort()
        n = len(a)
        m = len(b)
        i=j=0
        flag = True 
        while i < n and j < m:
            if a[i][0] <= b[j][0]:
                if a[i][1] == b[j][1]:
                    i += 1 
                    j += 1 
                elif a[i][1] > b[j][1]:
                    a[i][1] -= b[j][1]
                    j += 1 
                else:
                    b[j][1] -= a[i][1]
                    a[i][1] = 0 
                    i += 1 
            else:
                flag = False 
                break 
        if flag:
            return True 
        b = [[i,j] for i,j in a_.items()]
        a = [[i,j] for i,j in b_.items()]
        a.sort()
        b.sort()
        n = len(a)
        m = len(b)
        i=j=0
        flag = True 
        while i < n and j < m:
            if a[i][0] <= b[j][0]:
                if a[i][1] == b[j][1]:
                    i += 1 
                    j += 1 
                elif a[i][1] > b[j][1]:
                    a[i][1] -= b[j][1]
                    j += 1 
                else:
                    b[j][1] -= a[i][1]
                    a[i][1] = 0 
                    i += 1 
            else:
                flag = False 
                break
        return flag
                    
                
            
        