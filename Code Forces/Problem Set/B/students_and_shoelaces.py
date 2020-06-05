# https://codeforces.com/contest/129/problem/B
from collections import OrderedDict


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = OrderedDict()
    for i in range(1, n + 1):
        G[i] = set()

    for i in range(m):
        a, b = map(int, input().split())
        G[a].add(b)
        G[b].add(a)

    flag = False
    count = 0
    while True:
        topop = []
        for g in G:
            if len(G[g]) == 1:
                topop.append(g)
        if len(topop):
            for a in topop:
                if len(G[a]):
                    # print(G[a])
                    b = G[a].pop()
                    G.pop(a)
                    G[b].remove(a)
        else:
            break

        count += 1

    print(count)
