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
    def getInputArray():
        return list(map(int, input().split()))
    def getIntegerInputs():
        return map(int, input().split())
    def getInputIntegerMatrix(n):
        matrix = []
        for i in range(n):
            matrix.append(list(map(int,input().split())))
        return matrix
    def getInputStringMatrix(n):
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
6 3
001100001 
"""



def solve(t):
    n, k = getIntegerInputs()
    string = input()
    one = 0  
    zero = 0 
    for i in string:
        if i == '1':
            one += 1 
        elif i == '0':
            zero += 1 
    newstring = ''
    k1 = (k*zero//(n))
    k2 = (k*one//(n))
    if  k1 + k2 != k:
        print(IMPOSSIBLE)
        return 
    
    for i in range(k1):
        newstring += '0'
    for i in range(k2):
        newstring += '1'
    j = 0 
    for i in range(0,n,k):
        if j%2 == 0:
            print(newstring, end = '')
        else:
            for char in reversed(newstring):
                print(char, end = '')
        j += 1
    print()
                

    

if __name__ == '__main__':
    for t in range(int(input())):
        solve(t+1)
    