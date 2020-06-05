n, k = map(int, input().split())
h = list(map(int, input().split()))
s = float("inf")
index = None
sm = 0
for i in range(k):
    sm += h[i]
    index = 0
j = 0
s = sm
for i in range(k, n):
    # print(i, j)
    # print(sm)
    sm -= h[j]
    sm += h[i]
    # print(sm)
    j += 1
    if sm < s:
        sm = s
        index = j


print(index + 1)
