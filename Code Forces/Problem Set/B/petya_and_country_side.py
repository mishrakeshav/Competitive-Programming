n = int(input())
h = *map(int, input().split()),
count = 1

for i in range(n):
    x = y = h[i]
    k = j = i
    while j - 1 >= 0 and h[j - 1] <= x:
        j -= 1
        x = h[j]
    while k < n and h[k] <= y:
        y = h[k]
        k += 1
    count = max(count, k - j)
print(count)
