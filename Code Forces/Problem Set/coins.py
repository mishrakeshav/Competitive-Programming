

r1 = input()
r2 = input()
r3 = input()
s = [r1, r2, r3]
d = {}
r = "Impossible"
for A in range(3):
    for B in range(3):
        for C in range(3):
            if all([eval(x) for x in s]):
                d[A] = 'A'
                d[B] = 'B'
                d[C] = 'C'
                r = d[0] + d[1] + d[2]

print(r)
