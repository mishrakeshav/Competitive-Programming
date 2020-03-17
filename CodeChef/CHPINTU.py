for t in range(int(input())):
      N,M = map(int,input().split())
      F = list(map(int,input().split()))
      P = list(map(int,input().split()))
      costs = {}
      for i in range(N):
            if F[i] in costs:
                  costs[F[i]] += P[i]
            else:
                  costs[F[i]] = P[i]
      print(min(costs.values()))