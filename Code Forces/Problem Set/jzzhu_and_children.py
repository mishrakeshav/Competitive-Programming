from collections import deque
n,m = map(int,input().split())
a = list(map(int,input().split()))
queue = deque()
for i in range(n):
    queue.append([a[i],i])

last = None
while queue:
    
    c = queue.popleft()
    if c[0] > m:
        c[0] = c[0] - m
        queue.append(c)

print(c[1]+1)


