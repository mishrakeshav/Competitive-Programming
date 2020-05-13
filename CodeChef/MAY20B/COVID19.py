import math
for t in range(int(input())):
	n = int(input())
	x = list(map(int,input().split()))
	best_case = math.inf
	worst_case = 1
	count = 1
	x.sort()
	for i in range(1,n):
		if abs(x[i] - x[i-1]) <= 2:
			count += 1
		else:
			best_case = min(best_case,count)
			worst_case = max(worst_case,count)
			count = 1
	best_case = min(best_case,count)
	worst_case = max(worst_case,count)
	print(best_case,worst_case)
			
		
	