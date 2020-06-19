

if __name__ == '__main__':
    n = int(input())
    x = None 
    g = None
    start = 0 
    end = n
    while not x:
        y = (start+end)//2 
        print(y)
        g = input()
        if g == 'E':
            break
        if y + 1 <= end and g != 'E':
            print(y + 1)
            g = input()
        if g == 'L':
            end = y - 1 
        elif g == 'G':
            start = y + 1 
        else:
            x = True 
        
        
        
        