def solve():
    n = int(input())
    a = list(map(int,input().split()))
    s = int(input())
    limit = 1 << n 
    subset = 0 
    flag = True
    for mask in range(limit):
        subset = 0 
        for i in range(n):
            f = 1 << i 
            if f&mask:
                subset += a[i]
        if subset == s:
            print('YES')
            flag = False 
            break
    if flag:
        print('NO')


if __name__ == '__main__':
    for t in range(int(input())):
        solve()
