
def isValid(n, m, x, y, dx, dy):
    return 1 <= x + dx <= m and 1 <= y + dy <= n


if __name__ == '__main__':
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    k = int(input())
    d = []
    for i in range(k):
        dx, dy = map(int, input().split())
        d.append([dx, dy])
    count = 0
    for dx, dy in d:

        while isValid(n, m, x, y, dx, dy):
            print('Count =', count)
            print(x, y)
            print(dx, dy)

            x += dx
            y += dy
            count += 1
        print(x, y)

    print(count)
