def sequence(A, N):
      return set(A[:N//2 +1]) =={1, 2, 3, 4, 5, 6, 7}
def palindrome(A, N):
      for i in range(N//2 +1):
            if A[i] != A[N-i-1]:
                  return False
      return True
      
for t in range(int(input())):
      
      N = int(input())
      A = list(map(int, input().split()))
      
      if sequence(A,N) and palindrome(A, N):
            print('yes')
      else:
            print('no')