
N = 10**7 
prime = [1 for i in range(N+1) ]
p = 2
c = 0 

prefix = [0 for i in range(N+1)]
prefix[1] = 1 
for p in range(2,N+1):
    if (prime[p] == 1):
        c += 1 
        for i in range(p * p, N+1, p):
            prime[i] = 0
    prefix[p-1] = c 
    p += 1

for t in range(int(input())):
    n = int(input())
    if(n==2):
        print(1)
        continue
    if(n==3):
        print(2)
        continue
    ans = prefix[n] - prefix[n//2] + 1 
    print(ans)
