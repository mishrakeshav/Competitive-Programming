for t in range(int(input())):
    X,Y,K,N = map(int,input().split())
    flag = None
    for k in range(N):
        P,C = map(int,input().split())
        if P >= X - Y and C <= K :
            flag = True 
    if flag :
        print("LuckyChef")
    else:
        print("UnluckyChef")
