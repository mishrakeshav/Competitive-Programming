

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        point_a = 0
        point_b = 0
        for i in range(n):
            a,b = map(int,input().split())
            pow_a = 0 
            pow_b = 0 
            for s in str(a):
                pow_a += int(s)
            for s in str(b):
                pow_b += int(s)
            if pow_a > pow_b:
                point_a += 1 
            elif pow_a < pow_b:
                point_b += 1 
            else:
                point_a += 1 
                point_b += 1 

        if point_a > point_b:
            print(0,point_a)
        elif point_a < point_b:
            print(1,point_b)
        else:
            print(2,point_a)
