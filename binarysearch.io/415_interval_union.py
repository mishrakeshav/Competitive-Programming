class Solution:
    def solve(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        total = 0 
        INF = float('inf')
        prev,next = 0,-float('inf') 
        merged = []
        for a,b in intervals:
            print(next,prev)
            if next < a:
                if next==-float('inf') and prev==0:
                    pass 
                else:
                    merged.append([prev,next]) 
                prev = a 
                next = b 
            elif next >= a:
                next = max(next,b)
        merged.append([prev,next])
        return merged