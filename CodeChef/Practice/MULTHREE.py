for t in range(int(input())):
    k,d0,d1 = map(int,input().split())
    s = d0 + d1 

    c = ((2*s)%10) + ((4*s)%10) + ((8*s)%10) + ((6*s)%10) 
    cycles = (k-3)//4 
    total = 0 
    if k == 2:
        total = s 
    else:
        total = s + s%10 + (c*cycles)
        lo = k - 3 - (cycles*4)
        p = 2
        for i in range(lo):
            total += (p*s)%10
            p = (p*2)%10 
        
    if total%3 == 0:
        print("YES")
    else:
        print("NO")
