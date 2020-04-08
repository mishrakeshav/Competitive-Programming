#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
class Solution:
    def isHappy(self, n: int) -> bool:
        attractors = {4:0, 16:0, 37:0, 58:0, 89:0, 145:0, 42:0, 20:0}
        summ = n
        while True:
            s = summ
            summ = 0
            for i in str(s):           
                summ += int(i)*int(i)
            if summ in attractors:
                return False 
            elif summ == 1:
                return True
        
        