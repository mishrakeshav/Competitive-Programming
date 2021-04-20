from collections import Counter 
for t in range(int(input())):
    # print('text',t+1)
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    freq = Counter(a)

    for i in freq:
        if freq[i] > x:
            freq[i] -= x 
            x = 0 
        elif freq[i] <= x:
            x -= freq[i]
            x += 1 
            freq[i] = 1 

        if x == 0:
            break 
    if x:
        for i in freq:
            if x:
                x -= freq[i]
                freq[i] = 0 
            else:
                break 

    ans = 0 
    for i in freq:
        if freq[i]:
            ans += 1 
    print(ans)


    