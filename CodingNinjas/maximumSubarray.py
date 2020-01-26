for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    newArr = [0]*n 
    newArr[n-1] = arr[n-1]
    for i in range(n-2,-1, -1):
        
        if(arr[i] < arr[i] + newArr[i+1]):
            newArr[i] = arr[i] + newArr[i+1]
        else:
            newArr[i] = arr[i]
    print(max(newArr))




    