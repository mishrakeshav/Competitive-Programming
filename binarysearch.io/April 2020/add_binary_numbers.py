class Solution:
    def solve(self, a, b):
        a= list(map(int, list(a)))[::-1]
        b = list(map(int, list(b)))[::-1]
        s = 0
        cy = 0
        i = 0
        j = 0
        ans = ""
        
        while(i<len(a) and j<len(b)):
            s = a[i] + b[j] + cy
            if s == 0:
                ans += '0'
                cy = 0
            elif s == 1:
                ans += '1'
                cy = 0
            elif s == 2:
                cy = 1
                ans += '0'
            elif s == 3:
                cy = 1
                ans += '1'
            i += 1
            j += 1
        while(i < len(a)):
            s = a[i] + cy
            if s == 0:
                ans += '0'
            elif s == 1:
                ans += '1'
                cy = 0
            elif s == 2:
                ans += '0'
                cy = 1
            i += 1
            
        while(j < len(b)):
            s = b[i] + cy
            if s == 0:
                ans += '0'
            elif s == 1:
                ans += '1'
                cy = 0
            elif s == 2:
                ans += '0'
                cy = 1
            j += 1
        
        if cy:
            ans += '1'
            
        return ans[::-1]
