def merge_sort_helper(arr, start, end):
    if end > start:
        mid = (start + end)//2
        merge_sort_helper(arr, start , mid)
        merge_sort_helper(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    i = start
    j = mid + 1
    if (arr[mid] <= arr[mid+1]): 
        return;
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            i += 1
        else:
            temp = arr[j]
            for k in range(j,i-1,-1):
                arr[k] = arr[k-1]
            arr[i] = temp
            i += 1
            j += 1
            mid += 1
            
def merge_sort(arr):
    """
        Inplace merge sort
        Best Case : O(nlogn) 
        Worst Case:O(nlogn) 
    """
    start = 0 
    end = len(arr) - 1
    merge_sort_helper(arr,start,end)
    

for t in range(int(input())):
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print(arr)