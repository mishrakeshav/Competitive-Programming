class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        arr = [0]*1002
        for i in startTime:
            arr[i] += 1 
        for i in endTime:
            arr[i+1] -= 1
        for i in range(1,1002):
            arr[i] += arr[i-1]
        return arr[queryTime]
        
