#https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
for t in range(int(input())):
    n = int(input())
    i = 5
    count = 0
    while n//i >=1:
        count += n//i
        i *= 5
    print(count)

