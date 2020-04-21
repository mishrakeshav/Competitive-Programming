from sys import stdin
input = stdin.readline
for t in range(int(input())):
    n = int(input())
    if (n//2)%2:
        print('NO')
    else:
        i = 2
        j = n//2
        arr1 = []
        arr2 = []
        odd = 1
        even = 2
        while j:
            if even - odd < 0:
                arr1.append(even)
                arr2.append(odd)
                even += 4
                odd = even - 1
            elif odd - even < 0:
                arr1.append(even)
                arr2.append(odd)
                odd += 4
                even = odd - 1
            j -= 1
        print('YES')
        for i in arr1:
            print(i,end = " ")
        for i in arr2:
            print(i, end = " ")
        print()





