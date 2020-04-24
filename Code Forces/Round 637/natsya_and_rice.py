from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n, a, b, c, d = map(int,input().split())

    c1 =  (a-b)*n <= (c - d) or (a-b)*n <= (c+d)
    c2 =   (a+b)*n >= (c - d) or (a+b)*n >= (c+d)
    c = (a-b)*n == (c - d) or (a-b)*n == (c+d) or (a+b)*n == (c - d) or (a+b)*n == (c+d)
    if c:
        print("YES")
    elif c1 and c2:
        print("YES")
    else:
        print("NO")