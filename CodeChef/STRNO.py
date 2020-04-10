#TODO
from sys import stdin
input = stdin.readline
def isPrime(n):
    if n == 1:
        return 0 
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0 
    return 1
# for t in range(int(input())):
#     X,K = map(int, input().split())

for t in range(int(input())):
    N = int(input())
    n = 0
    k = 0
    for i in range(1,N//2 + 2):
        if N%i==0:
            
            if isPrime(i):
                k+= 1
            n += 1 
    
    print(N,'--> ',n,k)



    