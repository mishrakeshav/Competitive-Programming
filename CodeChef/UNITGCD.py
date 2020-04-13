from sys import stdin
input = stdin.readline
for t in range(int(input())):
    N = int(input())

    if N < 4:
        print(1)
        print(3,1,2,3)
    else:
        print(N//2)
        print(3,1,2,3)
        for i in range(4,N,2):
            print(2,i,i+1) 
        if not N%2:
            print(1,N)