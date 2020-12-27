import math
def solve():
    a,b = map(int,input().split())
    odd1 = math.ceil(a/2)
    odd2 = math.ceil(b/2)
    even1 = a//2 
    even2 = b//2 
    print(even1*even2 + odd1*odd2) 

if __name__ == '__main__':
    for t in range(int(input())):
        solve()