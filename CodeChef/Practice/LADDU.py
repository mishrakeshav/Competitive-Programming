# MOD = 10**9+7
# sys.setrecursionlimit(10**9)
from sys import stdin
input = stdin.readline
for t in range(int(input())):
    activities , nationality = map(str,input().split())
    laddus = 0
    for activity in range(int(activities)):
        a = list(map(str,input().split()))
        if a[0] == "CONTEST_WON":
            laddus += 300 
            if int(a[1]) < 20:
                laddus += 20 - int(a[1])
        elif a[0] == "TOP_CONTRIBUTOR":
            laddus += 300 
        elif a[0] == "BUG_FOUND":
            laddus += int(a[1])
        elif a[0] == "CONTEST_HOSTED":
            laddus += 50 
    if nationality == "INDIAN":
        print(laddus//200)
    else:
        print(laddus//400)

