for t in range(int(input())):
    n = int(input())
    e = list(map(int,input().split()))
    e.sort()
    count = 0 
    no_of_groups = 0 
    for i in e:
        count += 1
        if count == i:
            no_of_groups += 1
            count = 0 
    
    print(no_of_groups)
