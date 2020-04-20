def selection_sort(arr):
    """
        Best Case : O(n^2) 
        Worst Case : (n^2) 
    """
    n = len(arr)
    for i in range(n):
        mi = i 
        for j in range(i+1,n):
            if arr[mi] > arr[j]:
                mi = j
        if mi != i :
            arr[mi],arr[i] = arr[i], arr[mi]
    
for t in range(int(input())):
    arr = list(map(int, input().split()))
    selection_sort(arr)
    print(arr)