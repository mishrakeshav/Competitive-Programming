class Solution:
    def solve(self, arr):
        color = [0]*len(arr)
        visited = [0]*len(arr)
        
        def bfs(start):
            stack = [start,]
            c = 0 
            while stack:
                new = []
                for node in stack:
                    for n in arr[node]:
                        if not visited[n]:
                            new.append(n)
                            visited[n] = 1 
                    color[node] = c 
                stack = new 
                c ^= 1 
        
        bfs(0)
        for i in range(len(arr)):
            for node in arr[i]:
                if color[node] == color[i]:
                    return False 
        return True 
        
            
        