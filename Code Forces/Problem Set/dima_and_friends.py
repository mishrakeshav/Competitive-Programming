n = int(input())
counts = list(map(int,input().split()))
count = sum(counts)
no_of_ways = 0
after_count = count%(n+1)

for i in range(1,6):
    if (count+i)%(n+1) != 1:
        no_of_ways += 1

print(no_of_ways)