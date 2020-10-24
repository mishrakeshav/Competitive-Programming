
def bubble_sort(arr):
    """
        Best Case : O(n) - When the array is already sorted
        Worst Case : (n^2) 
    """
    n = len(arr)
    while True:
        
        swap = 0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = 1
            
        if swap == 0:
            break


for t in range(int(input())):
    arr = list(map(int, input().split()))
    bubble_sort(arr)
    print(arr)