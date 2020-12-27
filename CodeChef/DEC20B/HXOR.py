def solve():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    setbits = [0]*32 
    resetPos = None 
    for i in range(n-1):
        num = a[i]
        resetPos = [0]*32 
        k = 0 
        while num>>k:
            if(num&(1<<k)):
                resetPos[k] += 1  
            k += 1
        k = 31 
        while k >= 0:
            if resetPos[k] and  setbits[k]:
                a[i] ^= (1<<k)
                setbits[k] -= 1  
            elif x and resetPos[k]:
                a[i] ^= (1<<k)
                x -= 1 
                setbits[k] += 1
            k -= 1 
    x = x%2
    if x:
        a[-2] ^= 1 
        setbits[0] += 1 
    for i in range(31,-1,-1):
        while setbits[i]:
            a[-1] ^= (1<<i)
            setbits[i] -= 1 
    print(*a)

if __name__ == '__main__':
    for t in range(int(input())):
        solve()