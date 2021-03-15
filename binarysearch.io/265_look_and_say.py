class Solution:
    def solve(self, n):
        num = '1'
        for i in range(n-1):
            count = 0 
            ans = ''
            new = num[0]
            for a in num:
                if new == a:
                    count += 1 
                else:
                    ans += str(count) + new
                    new = a 
                    count = 1 

            ans += str(count) + new 
            num = ans 
        return num  