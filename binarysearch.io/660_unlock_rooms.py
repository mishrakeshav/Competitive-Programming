class Solution:
    def solve(self, rooms):
        visited = [0]*(len(rooms))
        
        def dfs(i):
            visited[i] = 1 
            for j in rooms[i]:
                if visited[j]:
                    continue 
                dfs(j)
        
        dfs(0)
        return all(visited)