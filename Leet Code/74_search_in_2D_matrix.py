class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) 
        m = len(matrix[-1])
        l = n*m - 1 
        left,right = 0,l
        while left < right:
            mid = (left+right)//2 
            element = matrix[mid//m][mid%m]
            print(left,right,element)
            if element >= target:
                right = mid 
            else:
                left = mid + 1 
        return matrix[left//m][left%m] == target
        