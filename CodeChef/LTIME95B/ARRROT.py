n = int(input())
a = list(map(int,input().split()))
q = int(input())
s = sum(a)
K = 10**9 + 7 
for i in range(q):
    s *= 2 
    s %= K 
    print(s)