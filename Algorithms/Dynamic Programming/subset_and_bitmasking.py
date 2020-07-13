def solve():
    n = int(input())
    a = list(map(str,input().split()))
    limit = 1 << n  # 2^n 
    for mask in range(limit):
        s = 0
        for i in range(n):
            f = 1 << i 
            if mask&f:
                s += a[i]
        
    
if __name__ == '__main__':
    for t in range(int(input())):
        solve()