n = int(input())
for i in range(10,0,-1):
    if n%i:
        continue
    print(i)
    break
