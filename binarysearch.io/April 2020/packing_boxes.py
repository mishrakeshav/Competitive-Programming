class Solution:
    def solve(self, nums):
        # Write your code here
        boxes = []
        box = []
        
        if len(nums) == 0:
            return boxes
            
        if len(nums) == 1:
            boxes.append(nums)
            return boxes
            
        box.append(nums[0])
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                box.append(nums[i])
            else:
                boxes.append(box)
                box = []
                box.append(nums[i])
                
        if len(box):
            boxes.append(box)
        return boxes
