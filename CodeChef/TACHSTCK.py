N , D = map(int,input().split())
A = []
for i in range(N):
    A.append(int(input()))
A.sort(reverse = True)


count = 0
i = 0
while i < N - 1:
    if A[i] - A[i+1] <= D:
        count += 1 
        i += 2 
    else:
        i += 1

print(count)
    
        