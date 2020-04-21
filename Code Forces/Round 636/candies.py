from sys import stdin
input = stdin.readline
for t in range(int(input())):
    n = int(input())
    x = 1
    s = 1
    j = 1
    while True:
        if s != 1 and n%s==0:
            break
        j *= 2
        s = s + j
    x = n//s
    print(x)


