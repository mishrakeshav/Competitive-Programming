for t in range(int(input())):
      lapin = input()
      
      n = len(lapin)
      if n%2==0:
            l1 = lapin[:n//2]
            l2 = lapin[n//2 : ]
      else:
            l1 = lapin[:n//2 ]
            l2 = lapin[n//2 + 1: ]
      #print(l1)
      #print(l2)
      list1 = []
      list2 = []
      for i in l1 :
            list1.append(i)
      for i in l2:
            list2.append(i)
      #print(list1)
      #print(list2)
      list1 = sorted(list1)
      list2 = sorted(list2)
      
      
      if list1 == list2:
            print('YES')
      else:
            print("NO")