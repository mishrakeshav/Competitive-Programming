from copy import deepcopy 
def check(arr,k):
    for i in range(len(arr)):
        if arr[i] == arr[i-1] or arr[i] == '?' or int(arr[i]) >= k:
            return False
        return True
    
for t in range(int(input())):
    K = int(input())
    S = input()
    N = len(S)
    if N == 1:
        if S == '?': print(0)
        elif int(S[0]) < K : print(S)
        else: print("NO")
        continue
    if K == 1:
        if N==1 and (S[0] == '0' or S[0] == '?') : print('0')
        else: print('NO')
        continue
    arr = list(S)
    if K == 2:
        if N%2:
            print("NO")
            continue
        brr = deepcopy(arr)
        for i in range(N):
            if brr[i] == '?':
                brr[i] = str(i%2)
        if brr == ['0','1']*(N//2):
            print("".join(brr))
            continue
        brr = deepcopy(arr)
		for i in range(N): # 101010
			if brr[i]=='?':
				brr[i] = str(1 - i%2)
		if brr == ['1','0']*(N//2):
			print("".join(brr))
			continue
        print("NO")
        continue

    for i in range(N):
        if arr[i] == '?':
            for j in range(K):
                if arr[(i+1)%N] != str(j) and arr[i-1] != str(j):
                    arr[i] = str(j)
                    break
    if check(arr,K):
        print("".join(arr))
    else:
        print("NO")



