def dfs(node,c):
    visited[node] = 1
    color[node] = c  
    for nbr in graph[node]:
        if visited[nbr]==0:
            if not dfs(nbr,c^1): 
                return False
        elif color[nbr] == color[node]:
            return False
    return True 


for tt in range(int(input())):
    n,m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = []
    visited = [0 for i in range(n+1)]
    color = [0 for i in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = True 
    for i in range(1,n+1):
        if visited[i] == 0:
            if not dfs(i,0):
                ans = False
                break
    if ans:
        print('No suspicious bugs found!')
    else:
        print('Suspicious bugs found!')
    
