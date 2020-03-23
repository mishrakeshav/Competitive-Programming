#https://www.spoj.com/problems/STPAR/
#TODO
while True:
    n = int(input())
    if n == 0:
        break 
    w = list(map(int,input().split()))
    w_sorted = sorted(w)
    j = 0
    stack = []
    for i in range(n):
        if w[i] == w_sorted[j]:
            j += 1 
        elif len(stack) and stack[-1] == w_sorted[j]:
            stack.pop()
            j += 1 
        else:
            stack.append(w[i]) 
        # print(stack)
    flag = True
    while stack:
        # print(w_sorted[j])
        # print(stack[-1])
        if w_sorted[j] != stack.pop():
            flag = False 
        j += 1
    if flag :
        print("yes")
    else:
        print("no")
            



    