"""
Given a list of [x, y] coordinates in a cartesian plane, 
return whether the coordinates form a straight line segment.
"""

class Solution:
    def solve(self, coordinates):
        # Write your code here
        if len(coordinates) == 1 or len(coordinates) == 2:
            return True 
        
        (x1,y1),(x2,y2) = coordinates[0],coordinates[1]
        
        if x1 != x2:
            return all(
                    (y2-y1)*(x-x1) == (y-y1)*(x2-x1) for x,y in coordinates
                )
        
        
        return all(
                x == x1 for x,y in coordinates
            )
        
        
        