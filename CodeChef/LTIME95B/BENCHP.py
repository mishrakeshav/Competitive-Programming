from collections import Counter
for t in range(int(input())):
    n,w,wr = map(int,input().split())
    we = list(map(int,input().split()))
    freq = Counter(we)
    ans = wr 
    for i in freq:
        if freq[i]%2==0:
            ans += freq[i]*i 
    if ans >= w:
        print('YES')
    else:
        print('NO')
