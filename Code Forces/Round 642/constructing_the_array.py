def solve(a,l,r,k):
    if l == r:
        a[l] = k 
        return k 
    if (r-l+1)%2:
        a[(l+r)//2] = k 
    else:
        a[(l+r-1)//2] = k

    k = solve(a,l,r-1,k+1)
    k = solve(a,r+1,len(a)-1,k+1)
    return k

for t in range(int(input())):
    n = int(input())
    a = ["#"]
    for i in range(n):
        a.append(0)
    solve(a,0,n,1)
    print("".join(a))

