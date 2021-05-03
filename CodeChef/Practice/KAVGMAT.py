def make_prefix(matrix,n,m,prefix):
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] +  matrix[i-1][j-1] - prefix[i-1][j-1] 

def print_matrix(matrix):
    for l in matrix:
        print(*l)

def get_sum(prefix,y1,x1,y2,x2):
    return prefix[y2][x2] - prefix[y1-1][x2] - prefix[y2][x1-1] + prefix[y1-1][x1-1]

def condition(k,s):
    return s/((k+1)*(k+1)) >= K

for t in range(int(input())):
    n,m,K = map(int,input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    prefix = [[0 for i in range(m+1)] for i in range(n+1)]
    make_prefix(matrix,n,m,prefix)
    ans = 0 
    for i in range(n):
        for j in range(m):
            left,right = 0,min(n-i,m-j)
            while left < right:
                mid = (left + right)//2 
                s = get_sum(prefix,i+1,j+1,i+mid+1,j+mid+1)
                if condition(mid,s):
                    right = mid 
                else:
                    left = mid + 1 
            ans += min(n-i,m-j) - left
    print(ans)




