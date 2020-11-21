"""
You are given a list of integers weights representing peoples' 
weights and an integer limit representing the weight limit of one rocket ship.

Each rocketship can take at most two people.

Return the minimum number of rocket ships it would take to rescue everyone to Mars.

Example:
weights = [200, 300, 200]
limit = 400
It would take one rocket ship to take the two people whose weights are 200, 
and another to take the person whose weight is 300.
"""
class Solution:
    def solve(self, weights, limit):
        # Write your code here
        count = 0
        w = sorted(weights)
        
        i = 0
        j = len(w) - 1
        while i <= j:
            if i == j:
                count += 1
                break
            if w[i] + w[j] <= limit:
                i += 1
                j -= 1
                count += 1
            elif w[i] + w[j] > limit:
                j -= 1
                count += 1
        
        return count
            
        
        
        
        
        
            
            
