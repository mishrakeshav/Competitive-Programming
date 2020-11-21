"""
You are given n people represented as an integer from 0 to n - 1, 
and a list of friends tuples, where person friends[i][0] 
and person friends[i][1] are mutual friends.

Return whether everyone has at least one friend.
"""
class Solution:
    def solve(self, n, friends):
        # Write your code here
        have_friends = [False]*(n)
        for x,y in friends:
            have_friends[x] = True
            have_friends[y] = True
        
        return all(have_friends)
            
