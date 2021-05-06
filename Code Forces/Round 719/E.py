for tt in range(int(input())):
    cost1 = 0 
    cost2 = 0
    n = int(input())
    s = input()
    prefix = [0 for i in range(n+1)]
    ans = 0 
    for i in range(1,n+1):
        if s[i-1] == "*":
            prefix[i] = 1 + prefix[i-1]
        else:
            prefix[i] = prefix[i-1]
    for i in range(n):
        if s[i] == '.':
            ans += min(prefix[i+1],prefix[n]-prefix[i+1])
    print(ans)

    