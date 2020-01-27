#Given an array of integers, print sums of all subsets in it. 


def sum_of_subset(arr, l, r, sumOfSubset = 0):

    if l > r :
        print(sumOfSubset, end = " ")
        return 
    
    sum_of_subset(arr, l+1, r, arr[l] + sumOfSubset)
    sum_of_subset(arr, l+1, r, sumOfSubset)

for t in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    sum_of_subset(arr, 0, n-1)
    print()
