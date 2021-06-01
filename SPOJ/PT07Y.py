def dfs(node):
    if visited[node]:
        return 
    visited[node] = 1 
    for nbr in graph[node]:
        dfs(nbr)

n,m = map(int,input().split())
graph = dict()
for i in range(1,n+1):
    graph[i] = []
visited = [0 for i in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
if m != n-1:
    print('NO')
else: 
    dfs(1)
    isTree = True
    for k in range(1,n+1):
        if visited[k]==0:
            isTree = False
            break
    if isTree:
        print('YES')
    else:
        print('NO')