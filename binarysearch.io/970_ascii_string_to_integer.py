class Solution:
    def solve(self, s):
        num = ''
        ans = 0 
        import string 
        letters = string.ascii_letters 
        for i in s:
            if i not in letters:
                num += i 
            else:
                print(num)
                if num:
                    ans += int(num)
                num = ''
        if num:
            ans += int(num)
        return ans 