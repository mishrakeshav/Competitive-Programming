"""
Problem link: https://codeforces.com/contest/152/problem/B
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
    n, m = getIntegerInputs()
    matrix = getInputStringMatrix(n)
    flag = True 
    freq = set()
    count = 0 
    for string in matrix:
        candy = False
        dwarf = False 
        for i in range(len(string)):
            char = string[i]
            if char == 'S' and not dwarf:
                flag = False 
                break 
            elif char == 'G':
                dwarf = True 
                pos_dwarf = i + 1 
            elif char == 'S':
                candy = True 
                pos_candy = i + 1
            # print(char, dwarf, candy)
        if (not candy) or (not dwarf):
            flag = False
            break
        if not flag:
            print(-1)
            return 
        if (pos_candy - pos_dwarf) not in freq:
            freq.add(pos_candy-pos_dwarf)
            count += 1 
    if not flag:
        print(-1)
        return 
    
    print(count)
    



    

if __name__ == '__main__':
    solve()
    