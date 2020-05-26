if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        if n == 1 and m == 1:
            print(1)
        elif n % 2 == 0:
            print((n // 2) * m)
        elif m % 2 == 0:
            print((m // 2) * n)
        else:
            ans = (n // 2) * m + m // 2 + 1
            print(ans)
