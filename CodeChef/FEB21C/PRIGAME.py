import math,sys 
input = sys.stdin.readline
INT_MAX = 10**6 
sieve = [1]*(INT_MAX + 2)
primes = [0]*(INT_MAX + 2)
cnt = 0 
i = 2
sieve[0] = 0 
sieve[1] = 0 
while i*i <= INT_MAX + 1:
    if sieve[i]:
        j = i*2 
        while j <= INT_MAX:
            sieve[j] = 0 
            j += i 
    i += 1 

for i in range(1,INT_MAX + 1):
    primes[i] = primes[i-1]
    if sieve[i]:
        primes[i] += 1 

for t in range(int(input())):
    x,y = map(int,input().split())
    if primes[x] <= y:
        print('Chef')
    else:
        print('Divyam')