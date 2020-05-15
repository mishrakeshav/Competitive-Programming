n,d = map(int,input().split())

sticks = []
for i in range(n):
    sticks.append(int(input()))

sticks.sort()
i = 0 
j = 1
count = 0
while i < n and j < n:
    if sticks[j] - sticks[i] <= d:
        count += 1
        i += 2
        j += 2
    else:
        i += 1
        j += 1
print(count)

    



