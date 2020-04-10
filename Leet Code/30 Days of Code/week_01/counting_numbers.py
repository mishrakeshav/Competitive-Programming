class Solution:
    def countElements(self, arr: List[int]) -> int:
        numbers = [0]*1002
        for i in arr:
            numbers[i] += 1 
        count = 0
        for i in arr:
            if numbers[i+1] > 0:
                count += 1 
            
        return count