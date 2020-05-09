import math
for t in range(int(input())):
    N = int(input())
    S = list(map(int,input().split()))
    m = math.inf
    maximum_no_of_token = 0 

    for i in S:
        m = min(i,m)
        maximum_no_of_token += m
    print(maximum_no_of_token)
    




