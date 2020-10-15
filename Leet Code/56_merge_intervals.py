class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        n = len(intervals)
        intervals.sort()
        prev = intervals[0]
        ans = []
        for i in range(1,n):
            if prev[1] >= intervals[i][0]:
                if prev[0] > intervals[i][0]:
                    prev[0] = intervals[i][0]
                
                if prev[1] < intervals[i][1]:
                    prev[1] = intervals[i][1]
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        
        return ans 
                