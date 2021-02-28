class Solution:
    def solve(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        total = 0 
        INF = float('inf')
        prev,next = 0,-float('inf') 

        for a,b in intervals:
            print(next,prev)
            if next < a:
                if next==-float('inf') and prev==0:
                    pass 
                else:
                    total += next - prev + 1 
                prev = a 
                next = b 
            elif next >= a:
                next = max(next,b)
        total += next - prev + 1
        return total   