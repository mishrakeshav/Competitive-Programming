class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        else:
            can_reach = -1
            for i in range(len(nums)):
                can_reach = max(i + nums[i],can_reach)
                if can_reach < i + 1:
                    break
                
            if can_reach >= len(nums)-1:
                return True
            else:
                return False
                    
        
            
            
                
            
                
                    
                    
                
        
            
        