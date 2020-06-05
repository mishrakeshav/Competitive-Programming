import math


def solve():
    # posible r1
    n, *x = list(map(int, input().split()))
    # posible p1
    m, *y = list(map(int, input().split()))
    # possible p2
    k, *z = list(map(int, input().split()))
    A, B = map(int, input().split())
    r1 = max(x)
    p2 = min(z)
    ans = 0
    for p1 in y:
        ans = max(r1 * math.sqrt((B * p1 / (B * p1 + A * p2))), ans)
    print(ans)


if __name__ == '__main__':
    solve()
