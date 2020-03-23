for t in range(int(input())):
      N = int(input())
      P = list(map(int, input().split()))
      count = 0

      for i in range(N):
            if i == 0 :
                  count += 1
            elif(i == 1 and P[i] < P[0]):
                  count += 1
            elif(i==2 and P[i] < P[i-1] and P[i] < P[i-2]):
                  count += 1
            elif(i==3 and (P[i]<P[i-1] and P[i] < P[i-2] and P[i] < P[i-3])):
                  count += 1
            elif(i==4 and (P[i]<P[i-1] and P[i] < P[i-2] and P[i] < P[i-3] and P[i] < P[i-4])):
                  count += 1
            elif(i > 4 and (P[i]<P[i-1] and P[i] < P[i-2] and P[i] < P[i-3] and P[i] < P[i-4] and P[i] < P[i-5])):
                  count += 1

      print(count)

