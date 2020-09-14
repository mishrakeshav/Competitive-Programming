def query(prefix,a,b):
    if a == b == 0:
        return prefix[0]
    elif a == 0:
        return prefix[b]
    else:
        return prefix[b] - prefix[a-1]

if __name__ == '__main__':
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    prefix = []
    prefix.append(arr[0])
    for i in range(1,n):
        prefix.append(prefix[-1] + arr[i])
    for _ in range(q):
        a,b = map(int, input().split())
        ans = query(prefix,a-1,b-1)
        print(ans)


