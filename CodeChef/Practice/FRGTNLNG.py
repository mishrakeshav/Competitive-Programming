for t in range(int(input())):
      
      N, K = tuple(map(int, input().split()))
      
      F = input().split()
      md = list()
      for i in range(K):
            
            M = input().split()
            md.extend(M)
      for i in F:
            if i in md:
                  print('YES', end = ' ')
            else:
                  print('NO', end = ' ')
      print()
            
            