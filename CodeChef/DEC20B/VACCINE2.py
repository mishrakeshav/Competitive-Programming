import math
def solve():
    n,d = map(int,input().split())
    patients = list(map(int,input().split()))
    risky_p = 0 
    for i in patients:
        if i >= 80 or i <= 9:
            risky_p += 1 
    non_risky_p = n - risky_p
    print(math.ceil(risky_p/d) + math.ceil(non_risky_p/d))

if __name__ == "__main__":
    for t in range(int(input())):
        solve()