class Solution:
    def solve(self, nums):
        from queue import PriorityQueue as PQ
        q = PQ()
        for i in nums:
            q.put(i)
        total = 0 
        
        while not q.empty():
            first = q.get()
            # print(first)
            if q.empty():
                return total 
            second = q.get()
            total += first + second
            q.put(first+ second)