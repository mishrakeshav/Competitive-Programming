for t in range(int(input())):
    N,C = map(int,input().split())
    A = list(map(int,input().split()))
    if C >= sum(A):
        print("Yes")
    else:
        print("No")