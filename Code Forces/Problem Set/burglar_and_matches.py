n, m = map(int, input().split())
matches = []
for i in range(m):
    matches.append(list(map(int, input().split())))
matches.sort(key=lambda container: container[1], reverse=True)

count = 0
i = 0
j = 0
while i <= n and j < m:
    if matches[j][0] < n - i:
        i += matches[j][0]
        count += matches[j][0] * matches[j][1]
    else:
        count += (n - i) * matches[j][1]
        i = n
    j += 1
print(count)
