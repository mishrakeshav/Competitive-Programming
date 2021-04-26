for t in range(int(input())):
    n,m = map(int,input().split())
    paths = []
    
    for i in range(n):
        row = list(map(int,input().split()))
        for j in range(m):
            paths.append([row[j], i, j])
    paths.sort()
    order = []
    for i in range(n):
        order.append([-1 for i in range(m)])
    person = 0 
    for val,i,j in paths:
        prev = person
        while order[i][person] != -1:
            person += 1 
            person %= m 
        order[i][person] = val
        person = (prev + 1)%m 
    
    for i in range(n):
        for j in range(m):
            print(order[i][j], end = " ")
        print()


    