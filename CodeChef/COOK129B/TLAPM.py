arr = []
c = 1 
for i in range(1,1001):
    arr.append(c)
    c += i 
matrix = []
matrix.append(arr)
k = 2 
for i in range(2,1001):
    newarr = []
    c = k 
    for j in matrix[-1]:
        newarr.append(j + c)
        c += 1 
    matrix.append(newarr)
    k += 1 

for t in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    ans = 0 
    for i in range(x1,x2+1):
        ans += matrix[i-1][y1-1]
    
    for i in range(y1+1,y2+1):
        ans += matrix[x2-1][i-1]
    print(ans)
    