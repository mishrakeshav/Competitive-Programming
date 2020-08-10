"""
Problem link: https://codeforces.com/contest/1360/problem/D
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    m = None
    n, k = map(int,input().split())
    mx = n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i <= k:
                mx = min(mx, n // i)
 
            if n // i <= k:
                mx = min(mx, i)
 
    print(mx)







if __name__ == '__main__':
    for t in range(int(input())):
        solve()