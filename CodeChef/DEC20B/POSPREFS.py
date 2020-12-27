from math import ceil
def solve():
    n,k = map(int,input().split())
    ans = [ -i if i%2 else i for i in range(1,n+1) ]
    if k >= n//2:
        i = n-1
        k -= n//2 
        if i%2:
            i -= 1   
        while k > 0:
            ans[i] *=-1 
            i -= 2 
            k -= 1
        print(*ans)
    elif k < n//2:
        i = n-1
        k = n//2 - k 
        if i%2==0:
            i -= 1   
        while k > 0:
            ans[i] *=-1 
            i -= 2 
            k -= 1
        print(*ans)

if __name__ == '__main__':
    for t in range(int(input())):
        solve()