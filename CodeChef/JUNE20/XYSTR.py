

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()

        c = 1 
        m = 0 
        n = len(s)
        while c < n:
            if s[c] == 'x':
                if s[c-1] == 'y':
                    c += 2 
                    m += 1 
                else :
                    c += 1
            elif s[c] == 'y':
                if s[c-1] == 'x':
                    c += 2 
                    m += 1 
                else:
                    c += 1
            
        
        print(m)