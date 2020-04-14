for _ in range(int(input())):
    string = input()
    count = 0
    for i in string:
        if i == '1':
            count+=1
    if count%2==0:
        print("LOSE")
    else:
        print("WIN")
