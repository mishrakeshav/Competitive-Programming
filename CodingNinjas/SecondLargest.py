def secondLargest(arr,n):

    largest = -999
    slargest = -999 

    for i in range(n):
        
        if arr[i] > largest:
            slargest = largest 
            largest = arr[i] 
        
        if arr[i] > slargest and arr[i] < largest:
            slargest = arr[i] 

    return slargest


print(secondLargest([2, 2, 1], 3))