for t in range(int(input())):
    
    arr = list(map(int, input().split()))
    n = len(arr)
    
    maximum = -999999999999999999
    newMax = maximum
    maxsubsequence = 0
    minimum = maximum
    for i in range(n-1, -1, -1):
        # print("Array: ",arr[i])
        # print("SUm: ",arr[i]+maximum) 
        if arr[i] > 0:
            maxsubsequence += arr[i]
        elif arr[i] > minimum:
            minimum = arr[i]
        maximum = max(arr[i], arr[i]+maximum)
        
        if maximum > newMax:
            newMax = maximum
    if maxsubsequence == 0 and 0 not in arr:
        maxsubsequence = minimum
        
        
    print(newMax, maxsubsequence)

