for t in range(int(input())):
      
      N = int(input())
      strings = input()
      count = 0
      for i in strings:
            if i == '1':
                  count += 1
      ans = (count * (count+1))//2
      print(ans)