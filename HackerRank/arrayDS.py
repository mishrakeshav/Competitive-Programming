for t in range(int(input())):    
    arr = []
    for i in range(6):
            arr.append(list(map(int, input().split())))

    newArr = []
    maximum = -9**10
    for i in range(4):
        for j in range(4):
            frow = sum(arr[i][j:j+3])
            srow = arr[i+1][j+1]
            trow = sum(arr[i+2][j:j+3])
            # print(" ", arr[i][j:j+3], " ")
            # print(" ",arr[i+1][j+1]," ")
            # print(" ", arr[i+2][j:j+3], " ") 
            # print(frow+srow+trow, end = " ")
            # print()
        # print()
            if frow+srow+trow > maximum:
                maximum = frow+srow+trow 
            
    print(maximum)

    