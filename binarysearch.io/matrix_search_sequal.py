class Solution:
    def solve(self, matrix, target):
        # Write your code here
        def binary_search(target,array):
            n = len(array)
            start = 0 
            end = n - 1 
            while start < end:
                mid = (start + end)//2 
                if array[mid] == target:
                    return True 
                elif array[mid] > target:
                    end = mid - 1 
                elif array[mid] < target:
                    start = mid + 1 
            
            return None 
        
        for array in matrix:
            element = binary_search(target,array)
            if element:
                return element 
        return False
        
