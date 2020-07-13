for t in range(int(input())):
      N,K = map(int,input().split())
      M = list(map(int,input().split()))
      count = 0
      for i in M:
            if not (i+K)%7:
                  count += 1 
      print(count)
                  