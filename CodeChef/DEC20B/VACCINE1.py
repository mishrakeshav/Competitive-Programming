import math
def solve():
    d1,v1,d2,v2,p = map(int,input().split())
    m = min(d1,d2) - 1 
    if d1 > d2:
        d1,d2 = d2, d1
        v1,v2 = v2, v1 
    vp = 0
    diff = d2 - d1  
    vp = diff*v1 
    if vp >= p:
        print(math.ceil(p/v1) + m)
        return 
    p -= vp 
    print(math.ceil(p/(v1+v2)) + m + diff)

if __name__ == '__main__':
    solve()