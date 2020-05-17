n = int(input())
h = *map(int, input().split()),
cost = 0
cost += h[1]
e = h[1]
i = 2
while i < n:
    if h[i] > e:
        cost += h[i] - e
        e += h[i] - e
    else:
        e += e - h[i]
    i += 1
print(cost)
