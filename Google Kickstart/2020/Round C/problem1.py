for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    i = 0
    while i < n:
        if a[i] == k:
            j = k
            while i < n and a[i] == j and j >= 1:
                i += 1
                j -= 1
            if j == 0:
                count += 1
            if i == n:
                break
        else:
            i += 1
    print("Case #{}: {}".format(t + 1, count))
