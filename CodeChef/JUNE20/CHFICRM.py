

if __name__ == '__main__':
    for t in range(int(input())):
        count_five = 0 
        count_ten = 0 
        flag = False
        
        n = int(input())
        a = list(map(int,input().split()))

        for i in a:
            if i == 5:
                count_five += 1 
            elif i == 10:
                if count_five:
                    count_five -= 1 
                    count_ten += 1 
                else:
                    flag = True 
            elif i == 15:
                if count_ten:
                    count_ten -= 1 
                elif count_five >= 2:
                    count_five -=2
                else:
                    flag = True
            

            if flag:
                print("NO")
                break
        
        if not flag:
            print("YES")


            
