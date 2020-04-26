from sys import stdin
input = stdin.readline
"""

2525 1
2400 5

------------------------------------------------>d
0,?       A
         2400, 5                               2525
Ta = (2525-2400)/5 = 125 

V = 2525/125 = 101


300 2
120 60
60 90

------------------------------------------------->
0,?         60,90           120, 60       meet      300
            A               B
m = (60*60 - 120*90)/(60-90) = 240 < 300 
t = (300-120)/60 = 3
V = 300/3 = 100


100 2
80 100
70 10
---------------------------------------------------------->
0,?         70,10           80, 100       90,90      meet      100
m = (90*80 - 100*90)/(90-80)=180 > 100 
m = (100*70-10*80)/(100-10)  = 68 < 70 

t = (100-70)/10 = 3
V = 100/3 = 33.33

"""





for t in range(int(input())):
    d,n = map(int,input().split())
    horses = []

    for i in range(n):
        k,s = map(int,input().split())
        horses.append([k,s])

    sorted_horses = sorted(horses, key = lambda a:a[0], reverse = True)

    p,v = sorted_horses[0]
    for p1,v1 in sorted_horses:
        if v == v1:
            p,v = p1,v1
        else:
            x = (v*p1-v1*p)/(v-v1)
            if x > d or x < p1:
                p,v = p1,v1

    time = (d-p)/v
    velocity = d/time
    print("Case #%d: %.6f"%(t+1,velocity))




    