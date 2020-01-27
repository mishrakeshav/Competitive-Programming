queue = []
for q in range(int(input())):
    queries = list(map(int, input().split()))
    if queries[0]== 1:
        queue.append(queries[1])
    elif queries[0]==2:
        queue.pop(0)
    else:
        print(queue[0])