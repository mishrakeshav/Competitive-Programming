

if __name__ == '__main__':
    for t in range(int(input())):
        n, x = map(int,input().split())
        arr = list(map(int,input().split()))
        y = x
        z = x
        arr.sort()
        flag = True 
        i = 0
        count1 = 0
        while i < len(arr):
            if x >= arr[i]:
                x = arr[i]
                i += 1 
            x *= 2 
            count1 += 1
        i = 0 
        count2 = 0
        while i < len(arr) and arr[i] >= y:
            i += 1 
        j = i 

        while i < len(arr):
            if y >= arr[i]:
                
                i += 1 
            y *= 2 
            count2 += 1
        count2 += (j + 1)
        if j == len(arr):
            count2 = float("inf")
        count3 = 0
        i = len(arr) - 1
        while arr[i] > z:
            z *= 2
            count3 += 1
        count3 += i - 1
        count = min(count1, count2, count3)
        print(count)




    
        

        

                        

                        
                        
                



    
        

        