# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass 

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n 
        if start == end:
            return start
        while start <= end:
            mid = (start+end)//2 
            if guess(mid) == 0:
                return mid 
            elif guess(mid) == -1:
                end = mid - 1
            elif guess(mid) == 1:
                start = mid + 1
            