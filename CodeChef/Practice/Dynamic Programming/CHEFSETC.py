"""
https://www.codechef.com/problems/CHEFSETC 
Type : Dynamic Programming
"""
def solve():
    a = list(map(int,input().split()))
    limit = 1 << 4 
    flag = True
    for mask in range(1,limit):
        s = 0 
        for i in range(4):
            f = 1 << i 
            if mask&f:
                s += a[i]
        if s == 0:
            print('Yes')
            flag = False 
            break
    if flag:
        print('No')

if __name__ == '__main__':
    for t in range(int(input())):
        solve()