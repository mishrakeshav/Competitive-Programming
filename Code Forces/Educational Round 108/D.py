from sys import stdin,stdout
input = stdin.readline
def output(x):
    stdout.write(str(x))

n = int(input())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

prefix = [0]
for i in range(n):
    prefix.append(prefix[i] + arr[i]*brr[i])
ans = prefix[n]
for k in range(n):
    curr = arr[k]*brr[k]
    i = k - 1 
    j = k + 1 
    while i>=0 and j < n:
        curr += arr[i]*brr[j]
        curr += arr[j]*brr[i]
        ans = max(ans,curr + prefix[i] + prefix[n]-prefix[j+1] )
        i -=1 
        j += 1 
    
    curr = 0 
    i = k
    j = k + 1 
    while i>=0 and j < n:
        curr += arr[i]*brr[j]
        curr += arr[j]*brr[i]
        ans = max(ans,curr + prefix[i] + prefix[n]-prefix[j+1] )
        i -=1 
        j += 1 
output(ans)

        
