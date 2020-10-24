def partition(arr, start,end):
    pivot = arr[start]
    i = start + 1
    j = end 
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        
        while i <=j and arr[j] > pivot:
            j -= 1

        if i <= j :
            arr[i],arr[j] = arr[j], arr[i]
        else:
            arr[start],arr[j] = arr[j], arr[start]
            return j


    
def quick_sort_helper(arr,start,end):
    
    if end - start > 1:
        p = partition(arr, start, end)
        quick_sort_helper(arr, start, p)
        quick_sort_helper(arr, p+1,end)
            
def quick_sort(arr):
    """
        Inplace merge sort
        Best Case : O(nlogn) 
        Worst Case:O(n^2) 
    """
    quick_sort_helper(arr,0,len(arr)-1)

    
    

for t in range(int(input())):
    arr = list(map(int, input().split()))
    quick_sort(arr)
    print(arr)