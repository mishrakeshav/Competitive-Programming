class Solution:
    def solve(self, courses):
        n = len(courses)
        def helper(start):
            visited[start] = 1 
            for v in courses[start]:
                if visited[v]==1:
                    return True 
                elif visited[v]==0:
                    if helper(v):
                        return True 
            
            visited[start] = 2 
            return False 
                    
                    
        
        visited = [0]*n 
        for i in range(n):
            # print(visited)
            if visited[i]==0 and helper(i):
                # print(visited)
                return False 
        return True 