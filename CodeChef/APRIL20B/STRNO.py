
from sys import stdin
input = stdin.readline
# cook your dish here
for t in range(int(input())):
    X, K = map(int, input().split())
    if K > X:
        print(0)
    elif X == K:
        print(1)
    else:
        count = 0
        n = X
        for i in range(2,int(n**0.5) + 1):
            while(n%i==0):
                count += 1 
                n /=i 
        if n > 1:
            count += 1
        if count >=K:
            print(1)
        else:
            print(0)
            
        
        
        



    