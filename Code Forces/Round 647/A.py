

if __name__ == '__main__':
    for t in range(int(input())):
        a,b = map(int,input().split())
        if a < b:
            a,b = b,a
        
        b = bin(b)[2:]
        a = bin(a)[2:]

        rem = len(a) - len(b)

        b += "".join(['0' for i in range(rem)])
        if int(a)^int(b) ==0:
            steps = 0 
            steps += rem//3 
            rem %= 3
            steps += rem//2 
            rem = rem%2 
            steps += rem 
            print(steps)
        else:
            print(-1)

