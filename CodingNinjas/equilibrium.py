
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))


    #Method 1
    rsum = sum(arr)-arr[0]
    lsum = 0
    # print(rsum,lsum)
    for i in range(n-1):
        lsum += arr[i]
        # print(lsum)
        rsum -= arr[i+1]
        # print(rsum)
        if lsum==rsum:
            print(i+1)
            break
    
    
    

