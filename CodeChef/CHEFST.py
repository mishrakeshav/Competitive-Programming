from sys import stdin
input = stdin.readline 

for t in range(int(input())):
    n1,n2,m = map(int,input().split())
    mi = min(n1,n2)
    s = m*(m+1)//2 
    
    s = min(s,mi)
    print(n1+n2 - 2*s) 
