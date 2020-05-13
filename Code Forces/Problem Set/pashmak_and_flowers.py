#TODO
import math
n = int(input())
b = list(map(int,input().split()))

i = 0 
j = n - 1
maximum = -math.inf
minimum = math.inf
for i in b:
    maximum = max(maximum,i)
    minimum = min(minimum,i)
count = 0
max_diff = maximum-minimum
counts = dict()
for i in b:
    if i not in counts:
        counts[i] = 0
    counts[i] += 1
count = 0
b = list(set(b))
for i in b:
    if i + max_diff  in counts:
        count += (counts[i]*counts[max_diff+i])
        counts[i] = 0
        counts[max_diff+i] = 0
print(max_diff,count)





    


