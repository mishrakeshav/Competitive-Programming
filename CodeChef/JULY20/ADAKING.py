


if __name__ == '__main__':
    for t in range(int(input())):
        k = int(input())
        count = 64 - k
        flag = True 
        for i in range(8):
            for i in range(8):
                if count > 0:
                    print('X', end = "")
                    count -= 1
                elif flag:
                    print("O", end = "")
                    flag = False 
                else:
                    print(".", end = "")
            print()
        
                
        
