
for t in range(int(input())):
    string = input()
    stack = [] 
    count = 0 
    max_count = 0

    for i in string:
        if i == "<":
            stack.append(i)
        else:
            if len(stack):
                stack.pop()
                count += 1
            else:
                stack = []
                max_count = max(count,max_count)
                count = 0
        
    max_count = max(count,max_count)
    print(max_count)
    
