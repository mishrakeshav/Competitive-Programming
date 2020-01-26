def prefixSum(arr,n, q):

    newArr = [0]*n 
    newArr[0] = arr[0]
    for i in range(n-1):
        newArr[i+1] = arr[i] + arr[i+1]

    print(newArr)
    for i in range(q):
        i, j = map(int, input().split())

        print(newArr[j] - newArr[i-1])

for t in range(int(input())):
    n , q = map(int, input().split())
    arr = list(map(int, input().split()))
    prefixSum(arr,n,q)


