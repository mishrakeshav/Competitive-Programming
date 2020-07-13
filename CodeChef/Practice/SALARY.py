for t in range(int(input())):
    N = int(input())
    W = list(map(int, input().split())) 
    
    print(sum(W)-N*min(W))