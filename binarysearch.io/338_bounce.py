class Solution:
    def solve(self, nums, k):
        visited = [0 for i in range(len(nums))]
        def dfs(nums,k):
            stack = [k,]
            while stack:
                new = []
                k = stack.pop()
                if visited[k]: continue 
                visited[k] = 1 
                if k == len(nums)-1:
                    return True 
                if 0 <= k + nums[k] < len(nums):
                    stack.append(k+nums[k])
                if 0 <= k - nums[k] < len(nums):
                    stack.append(k-nums[k])
            return False 
        
        return dfs(nums,k)