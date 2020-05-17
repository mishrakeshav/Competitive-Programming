import math
for t in range(int(input())):
    a,k = map(int,input().split())
    j = 0
    ai = 0
    while j < k:
        if j == 0:
            ai = a
        else:
            mx = 0
            mi = 9
            for i in str(ai):
                mx = max(mx,int(i))
                mi = min(mi,int(i))
            if int(mi) == 0:
                break
            ai += int(mx)*int(mi)
        j += 1
    print(ai)
