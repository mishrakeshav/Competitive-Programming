for t in range(int(input())):
    N = int(input())
    W = list(map(int,input().split())) 
    m = max(W)
    count1 = 0 
    count2 = 0
    for i in range(N):
        if W[i] == m:
            break 
        count1 += 1 
    for i in range(N-1,-1,-1):
        if W[i] == m :
            break 
        count2 += 1 
    # if count1 >= N//2:
    #     k = 0
    if count1+count2 >= N//2:
        k = count2
    else:
        k = 0 
    print(k) 





