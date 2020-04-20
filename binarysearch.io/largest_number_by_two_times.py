class Solution:
    def solve(self, nums):
        # Write your code here
        largest = -99999
        second = 0
        for i in nums:
            if i > largest:
                second = largest
                largest = i 
            
            if i < largest and i > second:
                second = i 
                
        return largest > 2*second
