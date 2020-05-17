n, a = map(int, input().split())
t = *map(int, input().split()),
max_distance = max(a, len(t) - a + 1)
a -= 1
count = 0
if t[a] == 1:
    count = 1
for d in range(1, max_distance):
    if a - d >= 0 and a + d < len(t):
        if t[a - d] and t[a + d]:
            count += 2
    elif a - d >= 0:
        if t[a - d]:
            count += 1
    elif a + d < len(t):
        if t[a + d]:
            count += 1

print(count)
