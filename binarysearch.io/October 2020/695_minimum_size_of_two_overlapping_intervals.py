class Solution:
    def solve(self, intervals):
        if len(intervals) == 1 or len(intervals) == 0:
            return 0 
        
        intervals.sort()
        
        # finding the size of each interval
        n = len(intervals)
        for i in range(n):
            s = intervals[i][1]-intervals[i][0] + 1
            intervals[i].append(s)
        
        min_size = float('inf')
        for i in range(n):
            # do binary search
            size = float('inf') 
              
        return min_size 
    
s = Solution()

print(s.solve([[1,4],[8,9],[3,5]]))
        
        

