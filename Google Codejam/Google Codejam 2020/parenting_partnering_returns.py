def order(timings, N):
    c = 0 
    j = 0 
    for i in range(N):
        if c <= timings[i][0]:
            timings[i].append("C")
            c = timings[i][1] 
        elif j <= timings[i][0]:
            timings[i].append("J")
            j = timings[i][1]
        else:
            return False 
    return timings
for t in range(int(input())):
    N = int(input())
    o = "" 
    timings = []
    for i in range(N):
        timings.append(list(map(int,input().split())) + [i])
    t_sorted = sorted(timings) 
    t_sorted = order(t_sorted, N)
    if t_sorted == False:
        o = "IMPOSSIBLE"
    else:
        o_task = sorted(t_sorted,key = lambda t : t[2])
        for i in o_task:
            o += i[3]
    print("Case #{}: {}".format(t+1,o))    

    


