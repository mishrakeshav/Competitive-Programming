class Solution:
    def solve(self, a, b):
        def multiply(x,y,c):
            m = x*y + c 
            return m//10,m%10
        e1,e2 = -1,-1
        si = 1 
        if a[0] == "-":
            e1 = 0
            si *=-1 
        if b[0] == "-":
            e2 = 0 
            si *=-1 
        n1 = len(a)
        n2 = len(b)
        final = 0 
        ans = ""
        c = 0 
        k = ""
        for i in range(n1-1,e1,-1):
            for j in range(n2-1,e2,-1):
                c,s = multiply(int(a[i]),int(b[j]),c)
                ans = str(s) + ans 
            if c:
                ans = str(c) + ans 
            final += int(ans)
            ans = k + "0"
            k += "0"
            c = 0 
        final *= si
        return str(final) 
            
                
                
        
            
            
        
            
                
        
        
            
            
            
        