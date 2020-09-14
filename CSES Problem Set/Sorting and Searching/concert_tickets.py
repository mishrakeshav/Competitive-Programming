"""
Problem link: 
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
from collections import Counter , deque
from queue import PriorityQueue
import math


helperConstants = True 
helperUtilityFunctions = True 

def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')
if helperConstants:
    YES = 'YES'
    NO = 'NO'
    yes = 'yes'
    no = 'no'
    true = 'true'
    false = 'false'
    FALSE = 'FALSE'
    TRUE = 'TRUE'
    IMPOSSIBLE = 'IMPOSSIBLE'
    POSSIBLE = 'POSSIBLE'
    INF = float('inf')

if helperUtilityFunctions:
    # Input utility functions
    def integers():
        return map(int, input().split())
    def integerArray():
        return list(map(int, input().split()))
    def integerMatrix(n):
        matrix = []
        for i in range(n):
            matrix.append(list(map(int,input().split())))
        return matrix
    def stringMatrix(n):
        matrix = []
        for i in range(n):
            matrix.append(input())
        return matrix

    # Output Utility functions
    def outputIntegerMatrix(matrix):
        for i in range(len(matrix)):
            print(*matrix[i])
    def outputStringMatrix(matrix):
        for i in range(len(matrix)):
            print(matrix[i])
    def kickstartoutput(testcase,*outputs):
        print('Case #%d:'%(testcase), *outputs)
"""
10 10
9 3 9 6 6 8 6 2 6 3
9 5 4 6 3 9 3 3 5 2

9 9 8 6 6 6 6 3 3 2
9 9 6 5 5 4 3 3 3 2
"""
    

def solve(t):
    n,m = integers()
    h = integerArray()
    t = integerArray()
    arr = []
    for i in range(m):
        arr.append([t[i],i,-1])
    h.sort(reverse=True)
    arr.sort(reverse=True, key = lambda x: x[0])
    i ,j = 0,0
    while i < n and j < m:
        if(h[i] <= arr[j][0]):
            arr[j][2] = h[i];
            i += 1
            j += 1 
        else:
            i += 1 
        
    arr.sort(key = lambda x: x[1])
    for i in arr:
        print(i[2])
    

    





if __name__ == '__main__':
    for t in range(1):
        solve(t+1)
    