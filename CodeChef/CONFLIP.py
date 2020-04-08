for t in range(int(input())):
    G = int(input())
    for g in range(G):
        I,N,Q = map(int,input().split())
        if I == 1 :
            if N%2:
                heads = N//2 
                tails = N - N//2 
                if Q == 1:
                    print(heads)
                else:
                    print(tails)
            else:
                print(N//2)
        else:
            if N%2:
                heads = N - N//2 
                tails =  N//2
                if Q == 1:
                    print(heads)
                else:
                    print(tails)
            else:
                print(N//2) 



        