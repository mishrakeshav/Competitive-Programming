
for t in range(int(input())):
    string = input()
    stack = [] 
    count = 0 
    ans = 0
    for i in range(len(string)):
        
        if string[i] == "<":
            count += 1 
        else:
            count -= 1 
            if count == 0 :
                ans = max(ans,i+1)
            elif count < 0:
                break
            


    print(ans)