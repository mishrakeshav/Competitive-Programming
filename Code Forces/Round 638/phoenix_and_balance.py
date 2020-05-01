for t in range(int(input())):
    n = int(input())
    s1 = 0
    s2 = 0
    i = 1
    j = n
    flag = 1
    if n == 2:
        print(2)
    elif (n//2)%2 == 0:
        while i < j:
            if flag == 1:
                s1 += 2**i + 2**j 
                flag = 2
            elif flag == 2:
                s2 += 2**i + 2**j 
                flag = 1
            i += 1
            j -= 1
        print(abs(s1-s2))
    else:
        m = n//2 
        i = 1
        flag = 1
        while i <= m :
            if flag == 1:
                s1 += 2**i 
                flag = 2
            elif flag == 2:
                s2 += 2**i 
            i += 1
        
        i = n 
        
        flag = 1
        while i > m + 1:
            if flag == 1:
                s1 += 2**i 
                flag = 2
            elif flag == 2:
                s2 += 2*i 
                flag = 1
            i -= 1
        s2 += 2**i
        print(abs(s1-s2))
        




