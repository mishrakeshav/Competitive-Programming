# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())
array = list(map(int, input().split()))
for i in range(M):
    q,l,r = map(int, input().split())
    if q==1:
        array = array[l-1:r] + array[:l-1] + array[r:]
        print(array)
    else:
        array = array[:l-1] + array[r:] + array[l-1:r] 
        print(array)

print(array[0]-array[-1])
for i in array:
    print(i,end = " ")