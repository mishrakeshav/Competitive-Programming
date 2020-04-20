class Solution:
    def solve(self, arr, target):
        # Write your code here
        
        n = len(arr)
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            if arr[0] > target:
                return 0
            elif arr[0] == target:
                return 0
            else:
                return 1
        elif arr[-1] < target:
            return n 
        for i in range(n):
            if arr[i] == target:
                return i
            elif arr[i] > target:
                return i 
        