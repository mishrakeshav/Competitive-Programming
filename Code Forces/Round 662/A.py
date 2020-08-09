"""
Problem link:
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')


"""
5
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1   = 5
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1

1 0 1 0 1 0 1
0 1 0 1 0 1 0
1 0 1 0 1 0 1
0 1 0 1 0 1 0
1 0 1 0 1 0 1  = 4
0 1 0 1 0 1 0
1 0 1 0 1 0 1


1 0 1 0 1 0
0 1 0 1 0 1 = 4
1 0 1 0 1 0
0 1 0 1 0 1
1 0 1 0 1 0
0 1 0 1 0 1

1 0 1 0 1
0 1 0 1 0
1 0 1 0 1  = 3
0 1 0 1 0
1 0 1 0 1

1 0 1 0
0 1 0 1
1 0 1 0  = 3
0 1 0 1

1 0 1
0 1 0  = 2
1 0 1

1 0
1 0 = 2

1
"""
def solve():
    n = int(input())
    if n == 1:
        print(n)
    else:
        count = 1
        print(count + (n//2))
        
            

if __name__ == '__main__':
    for t in range(int(input())):
        solve()