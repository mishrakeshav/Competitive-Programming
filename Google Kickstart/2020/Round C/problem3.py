for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            # print(s)
            sqrt = s**0.5
            # print(sqrt, int(sqrt))
            if sqrt == int(sqrt):
                count += 1
    print("Case #{}: {}".format(t + 1, count))
