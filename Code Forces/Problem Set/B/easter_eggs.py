n = int(input())
colors = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
c = "".join(colors)
w = "GBIV"
seq = c
count = 7
if count == n:
    print(seq)
else:

    c = 0
    for i in range(7, n):
        seq += w[c % 4]
        c += 1
    print(seq)
