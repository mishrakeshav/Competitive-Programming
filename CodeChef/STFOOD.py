from sys import stdin
input = stdin.readline 

for t in range(int(input())):
    N = int(input())
    S = []
    P = []
    V = []
    max_p = 0
    for i in range(int(N)):
        s,p,v = map(int,input().split())
        
        profit = (p//(s+1))*v 
        if profit > max_p:
            max_p = profit
    print(max_p)
        
