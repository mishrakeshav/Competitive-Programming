from sys import stdin
input = stdin.readline
def getSign(n):
    if n > 0:
        return 1
    else:
        return -1
for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    j = 0
    s = 0
    while i < n:
        curr = a[i]
        j = i
        while j < n and getSign(a[i]) == getSign(a[j]):
            curr = max(curr,a[j])
            j += 1
        s += curr 
        i = j 
        

    print(s)

