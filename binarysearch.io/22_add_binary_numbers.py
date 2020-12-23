class Solution:
    def solve(self, a, b):
        def bin_sum(x,y,c):
            x = int(x)
            y = int(y)
            c = int(c)
            si = (x+y+c)%2 
            c = (x+y+c)//2 
            if c:
                c = 1 
            return str(si),str(c)
        
         
        n , m = len(a),len(b)
        i,j = n-1,m-1
        ans = ''
        c = '0'
        while i >= 0 and j >= 0:
            si,c = bin_sum(a[i],b[j],c)
            ans = si + ans 
            i -= 1 
            j -= 1
        while i >= 0:
            if c:
                si,c = bin_sum(0,a[i],c)
                ans = si + ans 
            else:
                ans = a[:i+1] + ans 
            i -= 1
        while j >= 0:
            if c:
                si , c = bin_sum(0,b[j],c)
                ans = si + ans 
            else:
                ans = b[:j+1] + ans 
            j -= 1 
                
        ans = c + ans 
        ans = str(int(ans))
        return ans 
        
        