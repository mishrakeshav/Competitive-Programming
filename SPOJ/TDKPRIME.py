from sys import stdin,stdout
N = 87000008
primes = [1]*(N+1) 
primes[0] = 0 
primes[1] = 0 
for i in range(2,int(N**0.5)+1):
    if primes[i]:
        for j in range(i*i,N+1,i):
            primes[j] = 0 
prime_no = ["#"]
for i in range(N):
    if primes[i]:
        prime_no.append(i)
for q in range(int(input())):
    k = int(stdin.readline())
    stdout.write(str(prime_no[k]) + "\n")
    