class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 0 
        if n < 0:
            sign = 1 
        n = abs(n)
        ans = 1 
        ox = x 
        while n:
            if n%2:
                ans *= x 
                n -= 1 
                continue 
            x *= x 
            n //= 2  
        if sign:
            ans = 1/ans
        return ans 