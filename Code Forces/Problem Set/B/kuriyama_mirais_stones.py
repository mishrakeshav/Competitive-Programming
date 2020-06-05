def getSum(arr, l, r):
    if l == 0:
        return arr[r]

    return arr[r] - arr[l - 1]


if __name__ == '__main__':

    n = int(input())
    v = list(map(int, input().split()))
    m = int(input())
    u = sorted(v)

    prefix_v = []
    prefix_v.append(v[0])
    for i in range(1, n):
        prefix_v.append(prefix_v[i - 1] + v[i])

    prefix_u = []
    prefix_u.append(u[0])
    for i in range(1, n):
        prefix_u.append(prefix_u[i - 1] + u[i])

    for i in range(m):
        t, l, r = map(int, input().split())
        if t == 1:
            print(getSum(prefix_v, l - 1, r - 1))
        else:
            print(getSum(prefix_u, l - 1, r - 1))
