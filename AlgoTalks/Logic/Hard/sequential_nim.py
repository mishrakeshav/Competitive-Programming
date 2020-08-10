"""
Problem link: https://codeforces.com/problemset/problem/1382/B
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i == 1:
            count += 1 
    if count == n:
        if count%2:
            print('First')
        else:
            print('Second')
    else:
        if count%2:
            print('Second')
        else:
            print('First')
            
 

        
        
        


if __name__ == '__main__':
    for t in range(int(input())):
        solve()