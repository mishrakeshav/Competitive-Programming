for i in range(int(input())):
    N = int(input())
    flag = True
    for i in range(2,int(N**0.5)+1):
        if N%i==0:
            print("no")
            flag = False
            break 
    if flag:
        print("yes")