
def insertion_sort(arr):
    """
        Best Case : O(n) - When the array is already or mostly sorted
        Worst Case : (n^2) 
    """
    i = 1 
    n = len(arr)
    while i < n:
        temp = arr[i]
        j = i - 1 
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
        i += 1 




for t in range(int(input())):
    arr = list(map(int, input().split()))
    insertion_sort(arr)
    print(arr)