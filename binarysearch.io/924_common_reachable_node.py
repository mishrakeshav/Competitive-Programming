class Solution:
    def solve(self, edges, a, b):
        
        visiteda = dict()
        visitedb = dict()
        graph = dict()
        for x,y in edges:
            if x not in graph:
                graph[x] = set()
            if y not in graph:
                graph[y] = set()
            graph[y].add(x)
        def dfs_a(node):
            if node in visiteda:
                return 
            visiteda[node] = 1 
            for i in graph[node]:
                dfs_a(i)
        
        def dfs_b(node):
            if node in visiteda:
                return True 
            if node in visitedb:
                return 
            visitedb[node] = 1 
            for i in graph[node]:
                if dfs_b(i):
                    return True 
            return False 
        dfs_a(a)
        return dfs_b(b)