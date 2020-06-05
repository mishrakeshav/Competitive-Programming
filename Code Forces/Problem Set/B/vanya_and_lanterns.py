n, l = map(int, input().split())
a = set(map(int, input().split()))
a = list(a)
a.sort()
mi = -float("inf")
mi = max(a[0], l - a[-1])
for i in range(len(a) - 1):
    mi = max(mi, (a[i + 1] - a[i]) / 2)

print("%.10f" % (mi))
