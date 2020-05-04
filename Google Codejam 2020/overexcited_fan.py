import math
for t in range(int(input())):
    X, Y, M = map(str, input().split())
    X = int(X)
    Y = int(Y)
    steps_by_peppurr = [[X,Y,0]]
    count = 0
    x,y=X,Y
    for i in M:
        if i == 'N':
            count += 1
            y += 1
        elif i == "S":
            count += 1
            y -= 1
        elif i == "E":
            count += 1
            x += 1
        elif i == 'W':
            count += 1
            x -= 1
        steps_by_peppurr.append([x,y,count])
    steps_required = math.inf
    for x,y,step in steps_by_peppurr:
        if abs(x) + abs(y) <= step:
            steps_required = min(step,steps_required)
    
    if steps_required != math.inf:
        print("Case #{}: {}".format(t+1,steps_required))
    else:
        print("Case #{}: IMPOSSIBLE".format(t+1))
        
        
    
            
            
            
    
    
    