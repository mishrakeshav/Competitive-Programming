# Given an array of integers, calculate the fractions of its elements that 
# are positive, negative, and are zeros. Print the decimal value of each fraction 
# on a new line.

def plusMinus(arr):
    l = len(arr)
    countPositive = 0
    countNegative = 0
    countZeros = 0
    for i in arr:
        if(i>0):
            countPositive += 1 
        elif(i<0):
            countNegative += 1 
        else:
            countZeros += 1 
    print(round(countPositive/l,6))
    print(round(countNegative/l,6))
    print(round(countZeros/l,6))
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    plusMinus(arr)