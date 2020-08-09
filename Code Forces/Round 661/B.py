"""
Problem link:
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    moves = 0
    for i in range(n):
        a1 = a[i] - min_a
        b1 = b[i] - min_b
        moves += min(a1,b1)
        moves += abs(a1-b1)
    print(moves)

if __name__ == '__main__':
    for t in range(int(input())):
        solve()