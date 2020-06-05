
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    start = 0
    while start + 1 < n and a[start] < a[start + 1]:
        start += 1
    end = start
    while end + 1 < n and a[end] > a[end + 1]:
        end += 1
    b = a[:start] + a[start:end + 1][::-1] + a[end + 1:]
    a.sort()
    if a == b:
        print("yes")
        print(start + 1, end + 1)
    else:
        print("no")
