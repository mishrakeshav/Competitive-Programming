for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    counter = 0 
    flag = False
    result = True
    for i in A:
        if i == 1 and not flag:
            counter = 1
            flag = True 
        elif i == 1 and counter < 6 :
            result = False 
            break
        elif i == 1 and counter >= 6:
            counter = 1 
        else:
            counter += 1   
    if result:
        print("YES")
    else:
        print("NO")

        