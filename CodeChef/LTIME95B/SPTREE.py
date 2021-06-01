for t in range(int(input().split())):
    N,K,a = map(int,input().split())
    F = list(map(int,input().split()))
    tree = dict()
    for i in range(1,N+1):
        tree[i] = []
    for _ in range(N-1):
        a,b = map(int,input().split())
        tree[a].append(b)
    
    