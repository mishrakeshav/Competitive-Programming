"""
Problem link: https://codeforces.com/contest/1360/problem/A
"""

def solve():
    a, b = map(int,input().split())
    if b > a:
        a,b = b, a
    side = max(a,2*b)
    print(side**2)


if __name__ == '__main__':
    for t in range(int(input())):
        solve()