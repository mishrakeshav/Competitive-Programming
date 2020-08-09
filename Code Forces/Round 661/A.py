"""
Problem link:
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    flag = True 
    for i in range(1,n):
        if abs(a[i]-a[i-1]) > 1:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    for t in range(int(input())):
        solve()