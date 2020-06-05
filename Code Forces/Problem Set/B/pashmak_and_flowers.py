#TODO
import math
n = int(input())
b = list(map(int,input().split()))

maximum = -math.inf
minimum = math.inf
for i in b:
    maximum = max(maximum,i)
    minimum = min(minimum,i)

max_diff = maximum-minimum
count_mx = 0
count_mi = 0
for i in b:
    if i == maximum:
        count_mx += 1 
    elif i == minimum:
        count_mi += 1
if max_diff == 0:
    print(max_diff,n*(n-1)//2)
else:
    print(max_diff,count_mi*count_mx)







    


