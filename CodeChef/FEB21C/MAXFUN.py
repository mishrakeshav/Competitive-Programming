def solve():
    n = int(input())
    A = list(map(int,input().split()))
    A.sort()
    m = n//2
    mid = A[m] 
    print(abs(A[0] - mid) + abs(A[0]-A[-1]) + abs(A[-1]-mid))



if __name__ == '__main__':
    for t in range(int(input())):
        solve()