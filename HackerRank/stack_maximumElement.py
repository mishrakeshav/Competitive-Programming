stack = []

for q in range(int(input())):
    qrs = list(map(int, input().split()))

    if(qrs[0]==1):
        stack.append(qrs[1])
    elif(qrs[0]==2):
        stack.pop()
    else:
        print(max(stack))