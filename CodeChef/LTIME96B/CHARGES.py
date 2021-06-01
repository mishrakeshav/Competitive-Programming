for t in range(int(input())):
    n,k = map(int,input().split())
    s = list(input())
    q = list(map(int,input().split()))
    distance = 0 

    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            distance += 1 
        else:
            distance += 2 
    
    for i in range(k):
        idx = q[i]-1
        prev = s[idx]
        if idx != 0:
            if prev == s[idx-1]:
                distance -= 1 
            else:
                distance += 1 
        if idx!=len(s)-1:
            if prev == s[idx+1]:
                distance -= 1 
            else:
                distance += 1 
        if prev == '0':
            s[idx] = '1'
        else:
            s[idx] = '0'
        print(distance)
    