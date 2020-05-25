for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    diff = float("inf")

    for i in range(n - 1):
        if s[i + 1] - s[i] < diff:
            diff = s[i + 1] - s[i]

    print(diff)
