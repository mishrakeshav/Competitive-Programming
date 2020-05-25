import math
import string


def change(s, j, c):
    return s[:j] + c + s[j + 1:]


def check(b, a, n, m):
    for i in range(n):
        count = 0
        for j in range(m):
            if b[i][j] != a[j]:
                count += 1
            if count > 1:
                return 0
    return 1


def solve():
    n, m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(input())
    s = b[0]
    flag = 0
    for k in range(m):
        if flag == 1:
            break
        for c in string.ascii_lowercase:
            new = change(s, k, c)
            if check(b, new, n, m):
                flag = 1
                print(new)
                break
    if flag == 0:
        print(-1)


if __name__ == '__main__':
    for t in range(int(input())):
        solve()
