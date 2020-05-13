for t in range(int(input())):
    x,y,l,r = map(int,input().split())
    # f = (x&z)*(y&z)
    if x == 0 or y == 0:
        print(0)
    else:
        z = x | y 
        if z <= r:
            print(z)
        else:
            for z in range(l,r+1):
                if z & 1 == 0:
                    print(z)
                    break
                    
                
                
                
            