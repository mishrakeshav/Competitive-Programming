from sys import stdin,stdout
for t in range(int(stdin.readline())):
    N,Q = map(int, stdin.readline().split())
    A = list(map(int,stdin.readline().split()))
    for q in range(Q):
        x1,x2,y = map(int, stdin.readline().split())
        count = 0 
        for i in range(x1-1,x2-1):
            if y > A[i] and (A[i+1]>y or A[i+1] == y):
                count += 1 
            elif y < A[i] and (A[i+1] < y or A[i+1]==y):
                count += 1 
            else:
                if y == A[i]:
                    if A[i+1] > y or A[i+1] < y :
                        count += 1 
                    elif A[i+1] == y:
                        count += 1 
                        count += 1 
        print(count)
        
            
            

             
