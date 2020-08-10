"""
Problem link:https://codeforces.com/contest/1360/problem/B
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    m = float('inf')
    for i in range(1,n):
        m = min(m,abs(s[i-1]-s[i]))
    print(m)

if __name__ == '__main__':
    for t in range(int(input())):
        solve()