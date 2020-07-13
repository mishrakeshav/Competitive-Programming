if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        x = dict()
        y = dict()
        for i in range(4*n-1):
            a, b = map(int,input().split())
            if a not in x:
                x[a] = 0 
            if b not in y:
                y[b] = 0
            
            x[a] += 1
            y[b] += 1 
        for i in x:
            if x[i]%2:
                print(i, end =  " ")
                break
        for i in y:
            if y[i]%2:
                print(i)
        
             

        


        
