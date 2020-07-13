

"""

1. The count of numbers that are not  present in sequence 1 (c1 ) 
   and count of numbers that are not present in sequence 2 (c2) 
   should be equal and each element should be present even number of time 
   in either of the sequence
2. The minimum cost can be reduced by using the minimum element of 
    any of the sequences to swap the elements
3.

1 2 2 3 3 4 4          0
5 5 6 6 7 7 8

5 6 6 7 7 8 0          5
9 2 2 3 3 4 4


9
5 8 10 89 67 52 90 1888
1888 10 5 89 90 67 8  52
7
1 2 3 4 5 6 6
1 2 3 4 5 6 7
4
1 1 4 4 
2 2 3 3 
7
2 1 3 4 4 5 5 
2 3 1 6 7 6 7




0 
-1
4
9
"""


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int,input().split()))
        m = float("inf")
        A = dict()
        B = dict()
        for i in a:
            if i not in A:
                A[i] = 0 
            A[i] += 1 
            m = min(i,m)
        for i in b:
            if i not in B:
                B[i] = 0
            B[i] += 1
            m = min(i,m) 

        
        arr1 = []
        arr2 = []
        flag = False
        for i in A:
            if flag:
                break
            if i not in B :
                if A[i]%2:
                    flag = True
                else: 
                    for j in range(A[i]//2):
                        arr1.append(i)
            else:
                if A[i] > B[i]:
                    if((A[i]-B[i])%2):
                        flag = True
                    else:
                        for j in range((A[i]-B[i])//2):
                            arr1.append(i)
        for i in B:
            if flag:
                break
            if i not in A:
                if B[i]%2:
                    flag = True 
                else:
                    for j in range(B[i]//2):
                        arr2.append(i)
            else:
                if B[i] > A[i]:
                    if((B[i]-A[i])%2):
                        flag = True 
                    else:
                        for j in range((B[i] - A[i])//2):
                            arr2.append(i)
   

        if flag :
            print(-1)
        elif len(arr1) == len(arr2) == 0:
            print(0)
        else:
            arr1.sort()
            arr2.sort(reverse = True)
            cost = 0
            for i in range(len(arr1)):
                cost += min(arr1[i],arr2[i], 2*m)
            print(cost)

        



        




        




        








        
        



            
            
