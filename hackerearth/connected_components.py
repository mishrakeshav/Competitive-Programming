def dfs(i):
    if visited[i]:
        return 
    visited[i] = 1 
    for nbr in graph[i]:
        dfs(nbr)

n,e = map(int,input().split())
graph = dict()

visited = [0 for i in range(n+1)]
for i in range(1,n+1):
    graph[i] = []

for i in range(e):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

components = 1 
for i in range(1,n+1):
    if not visited[i]:
        components += 1 
        dfs(i)

print(components)
