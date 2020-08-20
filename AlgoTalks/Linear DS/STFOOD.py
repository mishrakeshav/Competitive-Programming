"""
Problem link: https://www.codechef.com/LRNDSA02/problems/STFOOD
Solution By Keshav Mishra 
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


def solve():
    n = int(input())
    max_profit = -float('inf')
    for i in range(n):
        s, p, v = map(int, input().split())
        max_profit = max(s//p*v, max_profit)
    print(max_profit)

    
    



if __name__ == '__main__':
    for t in range(int(input())):
        solve()