n = input()
count = 0
while len(n) > 1:
    s = 0
    for i in n:
        s += int(i)
    n = str(s)
    count += 1

print(count)
