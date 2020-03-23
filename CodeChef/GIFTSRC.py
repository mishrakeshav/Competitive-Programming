for t in range(int(input())):
    N = int(input())
    S = input()
    X,Y = 0,0 
  
    if S[0] in "LR" :
        flag = 0 
    else:
        flag = 1
    for s in S:
        if flag !=1:
            if s == 'L':
                X -= 1 
                flag = 1
            elif s == 'R':
                X += 1 
                flag = 1 
        elif flag != 0:
            if s == 'U':
                Y += 1
                flag = 0 
            elif s == 'D':
                Y -= 1 
                flag = 0 
        #print(X,Y)
    print(X,Y)
                


