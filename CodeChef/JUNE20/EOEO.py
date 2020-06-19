

if __name__ == '__main__':
    for t in range(int(input())):
        ts = int(input())
        count = 0
        while ts%2 == 0:
            ts //= 2 
        if ts:
            print(ts//2) 
        else:
            print(0)
        



        
