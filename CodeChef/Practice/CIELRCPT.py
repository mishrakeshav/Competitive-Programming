from sys import stdin
input = stdin.readline 

for t in range(int(input())):
    p = int(input())
    count = 0
    if p%2:
        count += 1 
        p -= 1 
    q = 2 
    while p:
        while p%q == 0 and q<= 2048:
            q *= 2 
        q /= 2 
        p -= q 
        q = 2 
        count += 1 
    print(count)
        
        

    