
# Brute Force Approach
# for t in range(int(input())):
#     N = int(input())
#     A = list(map(int, input().split()))
#     pairs = []
#     for i in range(N-1):
#         for j in range(N):
#             print(i , j)
#             if A[i]*A[j] == A[i] + A[j] :
#                 pairs.append([i,j])
#     print(pairs)


# Efficient method 
for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    count_zeros = 0 
    count_twos = 0 
    for i in A:
        if i==0:
            count_zeros += 1 
        elif i==2:
            count_twos += 1 

    total_count = (count_twos*(count_twos-1))//2 + (count_zeros*(count_zeros-1))//2
    print(total_count)


#testcase:
# 1 5 8 9 7 4 6 5 3 2 1 4 5 6 8 5 6 2 1 4 5 2 3 6 9 7 4 1 2 5   
#[ [9, 17], [9, 21], [9, 28],  [17, 21], [17, 28],  [21, 28]]