
for t in range(int(input())):
    n, a, b = map(int, input().split())
    for i in range(n):
        print(chr(ord('a') + i % b), end="")
    print()
