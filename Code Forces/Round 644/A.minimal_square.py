for t in range(int(input())):
    a, b = map(int, input().split())

    print(min(max(2 * a, b), max(2 * b, a))**2)
