def getdigits(n):
      elements = []
      while n!=0:
            rem = n%10
            n = n//10
            elements.append(rem)
      return elements
            
for t in range(int(input())):
      A, B = map(int, input().split())
       
      mydict = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
      S = getdigits(A+B)
      total = 0
      for i in S:
            total += mydict[i]
      print(total)
      