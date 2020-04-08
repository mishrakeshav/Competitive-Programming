from sys import stdin 
input = stdin.readline

N = int(input())
primes = [1]*(N+1) 
primes[0] = 0 
primes[1] = 0 
for i in range(2,int(N**0.5)+1):
    if primes[i]:
        for j in range(i*i,N+1,i):
            primes[j] = 0 
for i in range(N+1):
    if primes[i]:
        print(i,end = " ")
