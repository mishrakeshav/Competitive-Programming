import math
INT_MAX = 10**6 + 1 
SQRT_MAX = math.ceil(math.sqrt(INT_MAX))
sieve = [ 1 for i in range(INT_MAX) ]
primes = [ 0 for i in range(INT_MAX) ]
cnt = 0 
primes[0] = 0 
primes[1] = 0 
i = 2
while i*i <= INT_MAX:
    if sieve[i]:
        cnt += 1 
        j = i*2 
        while j <= INT_MAX:
            sieve[j] = 0 
            j += i 
    primes[i] = cnt

for t in range(int(input())):
    x,y = map(int,input().split())
    if primes[x] <= y:
        print('Chef')
    else:
        print('Divyam')