def solve(t):
    k = int(input())
    a = list(map(int,input().split()))
    count = 0
    c = 1
    ans = float("inf")
    for i in range(1,k):
        if a[i] > a[i-1]:
            if c == 4:
                count += 1 
            else:
                c += 1 
        elif a[i] < a[i-1]:
            if c == 1:
                count += 1 
            else:
                c -= 1 
    ans = min(ans,count)
    count = 0
    c = 2
    ans = float("inf")
    for i in range(1,k):
        if a[i] > a[i-1]:
            if c == 4:
                count += 1 
            else:
                c += 1 
        elif a[i] < a[i-1]:
            if c == 1:
                count += 1 
            else:
                c -= 1
    ans = min(ans,count)
    count = 0
    c = 3
    ans = float("inf")
    for i in range(1,k):
        if a[i] > a[i-1]:
            if c == 4:
                count += 1 
            else:
                c += 1 
        elif a[i] < a[i-1]:
            if c != 1:
                pass 

    ans = min(ans,count)
    count = 0
    c = 4
    ans = float("inf")
    for i in range(1,k):
        if a[i] > a[i-1]:
            if c == 4:
                c = 1
                count += 1
            else:
                c += 1 
        elif a[i] < a[i-1]:
            if c != 1:
                c-=1
    ans = min(ans,count)

    

        



    print("Case #{}: {}".format(t,ans))






if __name__ == '__main__':
    for t in range(int(input())):
        solve(t+1)