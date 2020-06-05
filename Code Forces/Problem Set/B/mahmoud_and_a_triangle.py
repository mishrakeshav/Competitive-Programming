
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    for i in range(n - 1, 1, -1):
        if a[i] + a[i - 1] > a[i - 2] and a[i - 2] + a[i - 1] > a[i] and a[i - 2] + a[i] > a[i - 1]:
            print("YES")
            exit()

    print("NO")
