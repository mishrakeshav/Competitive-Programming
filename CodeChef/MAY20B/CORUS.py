from collections import Counter
for t in range(int(input())):
    n,q = map(int,input().split())
    s = input()
    count = Counter(s)
    for i in range(q):
        c = int(input())
        size_of_pending_queue = 0
        for j in count:
            if count[j] > c:
                size_of_pending_queue += count[j] - c
        print(size_of_pending_queue)




			
	
	