for _ in range(int(input())):
    
    n = int(input());
    array = list(map(int, input()));
    i = 0
    for i in range(0, n):
        array[i], array[i+1] = array[i+1], array[i]
        i += 2
    i=0;sum=0
        
    for ele in array:
        summ += i*ele
        i +=1
    print(sum)
        
     