import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline 
def findmin(start,end):

    if start<=end:
        mid = (start+end)//2 
        left = findmin(start,mid-1)
        right = findmin(mid+1,end)
        return (left + right + end - start + 2)

    return 0
for t in range(int(input())):
    N , M = map(int,input().split())
    ul = 0 
    mi = findmin(0,N-1)
    mx = N*(N+3)//2
    if M > mx:
        print(M-mx)
    elif M >= mi and M <= mx:
        print(0)
    else:
        print(-1) 
