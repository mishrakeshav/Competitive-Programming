

if __name__ == '__main__':
    for t in range(int(input())):
        N = int(input())
        c  = 0
        if N%2:
            for i in range(N):
                for j in range(N):
                    print(c + j + 1, end = " ")
                c += N 
                print()
        else:
            for i in range(N):
                if i%2:
                    for j in range(N):
                        print(N + c - j, end = " ")

                else:
                    for j in range(N):
                        print(c + j + 1, end = " ")
                c += N

                print()
            

        
        