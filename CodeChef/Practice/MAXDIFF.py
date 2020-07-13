from sys import stdin
input = stdin

for t in range(int(input())):
    N,K = map(int,input().split())
    W = sorted(list(map(int,input().split())))

    b = min(K,N-K)
    a = sum(W[:b])
    print(sum(W[b:])-a)