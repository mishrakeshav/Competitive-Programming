"""
Problem link: http://codeforces.com/contest/186/problem/B
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
    
    


def solve():
    n, t1, t2, k = getIntegerInputs()
    participants = []
    k = 1 - k*0.01
    for i in range(n):
        a, b = getIntegerInputs()
        ans1 = 0
        ans2 = 0 
        ans1 += a*t1 
        ans1 = ans1*k
        ans1 += b*t2 
        ans2 += b*t1 
        ans2 = ans2*k 
        ans2 += a*t2 
        ans = max(ans1,ans2)
        participants.append({'index':i + 1, 'value':ans})
    participants.sort(reverse = True, key = lambda x : x['value'])
    for participant in participants:
        print('%d %.2f'%(participant['index'], participant['value']))




    
if __name__ == '__main__':
    solve()
    