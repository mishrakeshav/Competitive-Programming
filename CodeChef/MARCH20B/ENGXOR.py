from sys import stdin,stdout
oddEven = [0,1,1,0,1,0,0,1]
def countSetBits(n):
      
      if n>=0 and n <= 7:
            return oddEven[n]
      else:
            if n%2:
                  return 1 - countSetBits(n//2)
            else:
                  return countSetBits(n//2)
for t in range(int(stdin.readline())):
      countEven = 0
      countOdd = 0
      N,Q = map(int,stdin.readline().split())
      A = list(map(int,stdin.readline().split()))
      for a in A:
            if countSetBits(a):
                  countOdd += 1 
            else:
                  countEven += 1 
      for q in range(Q):
            P = int(stdin.readline())
            countP = countSetBits(P)
            if countP :
                  print(countOdd,countEven)
            else:
                  print(countEven,countOdd)
            

      

                  
            
            
            