for t in range(int(input())):
    N = int(input())
    P = sorted(list(map(int,input().split())), reverse = True)
    
    profit = 0 
    for i in range(N):
        if P[i] - i > 0 :
            profit += P[i] - i 
        else:
            break
    print(profit%1000000007)

