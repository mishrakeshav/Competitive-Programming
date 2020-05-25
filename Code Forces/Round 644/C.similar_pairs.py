from collections import Counter
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    count_odd = 0
    count_even = 0
    for i in a:
        if i % 2:
            count_odd += 1
        else:
            count_even += 1
    counts = Counter(a)

    if count_odd % 2 == 0 and count_even % 2 == 0:
        print("YES")
        continue

    if count_even % 2 and count_odd % 2:
        flag = 0
        for i in a:
            if i + 1 in counts or i - 1 in counts:
                flag = 1
                print("YES")
                break
        if flag == 1:
            continue

    print("NO")
