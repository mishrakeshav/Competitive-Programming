for tt in range(int(input())):
    n = int(input())
    u = list(map(int,input().split()))
    s = list(map(int,input().split()))
    students = [0 for i in range(n+1)]
    uni = dict()
    prefix = dict()
    for k in range(n):
        if u[k] not in uni:
            uni[u[k]] = []
            prefix[u[k]] = [0]
        uni[u[k]].append(s[k])
    
    for k in uni:
        uni[k].sort(reverse=True)
    for k in uni:
        for j in uni[k]:
            prefix[k].append(prefix[k][-1] + j)
        
    
    students = [0 for i in range(n+1)]
    for i in prefix:
        university = prefix[i]
        for k in range(1,len(university)):
            un = university
            x = len(un)-1
            if k <= x:
                y = (x//k)*k 
                students[k] += un[y]

    # for k in range(1,n+1):
    #     for un in prefix.values():
    #         x = len(un)-1
    #         if k <= x:
    #             y = (x//k)*k 
    #             students[k] += un[y]
        
    for i in range(1,n+1):
        print(students[i],end=" ")
    print()

