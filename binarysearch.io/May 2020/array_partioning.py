class Solution:
    def solve(self, s):
        # Write your code here
        red = 0
        green = 0
        blue = 0
        r = 0
        b = -1
        for i in s:
            if i == 'red':
                red += 1
            elif i == 'green':
                green += 1
            elif i == 'blue':
                blue += 1
        j = -1
        for i in range(red):
            j += 1
            s[j] = 'red'
        for i in range(green):
            j += 1
            s[j] = 'green'
        
        for i in range(blue):
            j += 1
            s[j] = 'blue'
            
        return s
            
