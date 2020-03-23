for t in range(int(input())):
      N = int(input())
      A = list(map(int, input().split()))
      max_stars = 0
      count = 0
      a = [1] * N

      for i in range(N - 1, 0, -1):
            count = 0
            if a[i]:
                  for j in range(i):
                        if(A[j] % A[i] == 0):
                              count += 1
                              a[j] = 0

                        if count > max_stars:
                              max_stars = count
      print(max_stars)P
