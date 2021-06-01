"""
1 7 
1 2 4
1 2 1 
"""
for t in range(int(input())):
    x,y = map(int,input().split())
    if y%x:
        print(-1)
        continue
    y //=x 
    flag = False
    ans = float('inf')
    low,high = 1,65 
    for i in range(1,65):
        tt = y + i 
        binary = bin(tt)[2:]
        if binary.count('1') == i:
            binary = binary[::-1]
            si = 0 
            for j in range(len(binary)):
                if binary[j] == '1':
                    si += j 
            si = si + i -1 
            ans = si 
            flag = True
            break
            
    if flag:
        print(ans)
    else:
        print(-1)

