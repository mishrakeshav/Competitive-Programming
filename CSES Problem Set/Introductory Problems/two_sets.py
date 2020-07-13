"""
Your task is to divide the numbers 1,2,…,n into two sets of equal sum.
soltn:
Add elements alternatively and check the final sum 
of the two sets 
"""
def solve(n):
    arr1 = []
    arr2 = []
    flag = 1 
    s2 = 0 
    s1 = 0
    
    for i in range(0,n,2): 
        
        if flag:
            arr1.append(i)
            arr2.append(i+1)
            s1 += i 
            s2 += i+1
            flag = 0
        else:
            s1 += i + 1 
            s2 += i
            arr1.append(i+1)
            arr2.append(i)
            flag = 1 
        
    if s1 == s2:
        print('YES')
        print(len(arr1)-1)
        for i in range(1,len(arr1)):
            print(arr1[i], end = " ")
        print()
        print(len(arr2))
        print(*arr2)
    else:
        print("NO") 

if __name__ == '__main__':
    n = int(input())
    
    solve(n)