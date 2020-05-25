for t in range(int(input())):
    n, k = map(int, input().split())

    mx = n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i <= k:
                mx = min(mx, n // i)

            if n // i <= k:
                mx = min(mx, i)

    print(mx)
