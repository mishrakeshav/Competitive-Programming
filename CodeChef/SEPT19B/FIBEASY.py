
for t in range(int(input())):
    n = int(input())
    if n==1:
        print(0)
    elif(n > 1):
        i = 1
        while True:
            if 2**i > n:
                i -= 1
                break
            else:
                i += 1
        n1 = i
        #print(n1)
        myrange1 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62]
        
        myrange2 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63]
        
        myrange3 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64]
        
        #print(myrange1[0:10])
        #print(myrange2[0:10])
        #print(myrange3[0:10])
        if n1==1:
            print(1)
        elif n1 in myrange1:
            print(2)
        elif n1 in myrange2:
            print(3)
        elif n1 in myrange3:
            print(0)
        else:
            print(9)
