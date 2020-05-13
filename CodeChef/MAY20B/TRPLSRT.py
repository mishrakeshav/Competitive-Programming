"""
1
9 4
2 3 7 9 8 4 1 5 6  
4
1 2 3 
4 9 6
1 7 5
1 8 5

1
8 4
8 7 6 5 4 3 2 1
4
1 8 2
1 7 2
3 6 4
3 5 4
"""
for t in range(int(input())):
    n,K = map(int,input().split())
    p = list(map(int,input().split()))
    count = 0
    rotated_elements = []
    cycle = []
    while count != K:
        flag = 0
        for i in range(n):
            if p[i] != i + 1:
                flag = 1
                v1 = i
                v2 = p[i] - 1
                v3 = p[p[i] - 1] - 1 
                if v2 != v3 :
                    rotated_elements.append([v1 + 1,v2+1 , v3 + 1])  
                    p[v1],p[v2],p[v3] = p[v3],p[v1],p[v2]
                    count += 1
                else:
                    if cycle:
                        v1,v2 = cycle
                        rotated_elements.append([v1 + 1,v2+1 , v3 + 1])  
                        p[v1],p[v2],p[v3] = p[v3],p[v1],p[v2]
                        count += 1
                    else:
                        cycle.append(v1,v2)
                
        
                    
            if count == K:
                break
            
        if flag == 0:
            break
    
    if all(p[i] == i + 1 for i in range(n)):
        print(len(rotated_elements))
        for a,b,c in rotated_elements:
            print(a,b,c)
    else:
        print(-1)
        




    

    

            





            
    




    