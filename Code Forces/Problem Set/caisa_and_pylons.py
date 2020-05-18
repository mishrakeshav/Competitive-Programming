n = int(input())
h = list(map(int, input().split()))
e = 0
x = 0
dollars_spent = 0
for i in range(n):
    y = h[i]
    e += x - y
    if e < 0:
        dollars_spent += abs(e)
        e = 0
    x = h[i]


print(dollars_spent)
