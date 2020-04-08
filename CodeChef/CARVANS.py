from sys import stdin,stdout
for t in range(int(stdin.readline())):
    N = int(stdin.readline())
    A = list(map(int,stdin.readline().split()))
    minimum = A[0]
    count = 0 
    for i in A:
        if i <= minimum:
            count += 1 
            minimum = i 
    stdout.write(str(count) + "\n")