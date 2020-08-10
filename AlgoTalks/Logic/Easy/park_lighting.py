"""
Problem link:
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n, m = map(int,input().split())
    if n%2 == 0:
        print((n//2)*m)
    elif m%2 == 0:
        print((m//2)*n)
    else:
        
        count = (n//2)*m  + (m//2)  + 1
        print(count)




if __name__ == '__main__':
    for t in range(int(input())):
        solve()