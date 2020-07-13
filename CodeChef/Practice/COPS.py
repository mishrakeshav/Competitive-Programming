for t in range(int(input())):
    m,x,y = map(int,input().split())
    M = list(map(int,input().split()))
    houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    
    for cop in M:
        for i in range(cop,cop+x*y+1):
            if i > 100:
                break
            houses[i] = 1
        for i in range(cop,cop-x*y-1,-1):
            if i < 0:
                break
            houses[i] = 1
    houses[0] = 0 
    
    print(100-houses.count(1))
