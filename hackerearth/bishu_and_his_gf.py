
def dfs(node,h):
    distance[node] = h + 1 
    for nbr in graph[node]:
        dfs(nbr,distance[node] + 1)

n = int(input())
graph = dict()
for i in range(1,n+1):
    graph[i] = []

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)

distance = [0 for i in range(n+1)] 
dfs(1,0)

q = int(input())
d,node = float('inf'),float('inf')
for _ in range(q):
    l = int(input())
    if distance[l] < d:
        d = distance[l]
        node = l 
    
    if distance[l] == d and l < node:
        node = l 
    
print(node)