"""
Problem link: 
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
from collections import Counter , deque
from queue import PriorityQueue

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

if helperUtilityFunctions:
    # Input utility functions
    def getInputArray():
        return list(map(int, input().split()))
    def getIntegerInput():
        return int(input())
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

def solve(t):
    pass 
    

if __name__ == '__main__':
    for t in range(int(input())):
        solve(t+1)
    