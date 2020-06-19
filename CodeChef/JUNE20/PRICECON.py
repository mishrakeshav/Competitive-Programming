

if __name__ == '__main__':
    for t in range(int(input())):
        n, k = map(int,input().split())
        p = list(map(int,input().split()))

        loss = 0 
        for i in p:
            if i > k:
                loss += i - k 
        
        print(loss)