for t in range(int(input())):
    l = int(input())
    s = input()
    flag = False
    c = 1
    k = 0   
    for i in s:
        k += int(i)
        if k/c*100 >= 50:
            flag = True 
            break
        c += 1 
    
    if flag:
        print('YES')
    else:
        print('NO')