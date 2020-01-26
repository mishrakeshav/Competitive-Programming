for _ in range(int(input())):
	N, K = tuple(map(int, input().split()))
	a1 = [0]*K
	n1 = N
	a2 = [0]*K
	n2 = N
	i=0
	while(i<K):
		a1[i] += 1
		n1 -= 1
		if(i<K-1):
			i += 1
		elif(i>=K):
			i=0
	i=0
	while(n2>=K):
		a2[i] += K
		n2 -= K
		if(i<K-1):
			i += 1
		elif(i>=K):
			i=0
	if(a1==a2):
		print("NO")
	else:
		print("YES")
		
		
	
		
	