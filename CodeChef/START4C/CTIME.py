def get_list():
    return list(map(int,input().split()))

for t in range(int(input())):
    n,k,f = get_list()
    intervals = []
    for i in range(n):
        se = get_list()
        intervals.append(se)
    intervals.sort()
    pb = 0
    kcount = 0 
    for a,b in intervals:
        if a > pb:
            kcount += a - pb 
        pb = max(pb,b)
    
    if f > pb:
        kcount += f - pb 
    if kcount >= k:
        print('YES')
    else:
        print('NO')
