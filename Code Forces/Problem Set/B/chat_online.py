
def solve():
    p, q, l, r = map(int, input().split())
    X = set()
    Z = set()
    for i in range(p):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            X.add(j)
    for i in range(q):
        c, d = map(int, input().split())
        for j in range(c, d + 1):
            Z.add(j)
    ans = 0
    for i in range(l, r + 1):
        for j in Z:
            if j + i in X:
                ans += 1
                break
    print(ans)


if __name__ == '__main__':
    solve()
