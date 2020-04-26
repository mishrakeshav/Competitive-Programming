
for t in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    cost = 0
    x1,y1 = x,y
    x = abs(x)
    y = abs(y)
    if x ==0 and y ==0:
        print(cost)
    elif x == y:
        print(b*abs(x))
    elif x == 0:
        cost = y*a
        print(cost)
    elif y == 0:
        cost = x*a
        print(cost)
    else:
        mx = max(x,y)
        mi = min(x,y)
        if x1 > 0 and y1 > 0:
            cost1 = mi*b + (mx-mi)*a
            cost2 = x*a + y*b
            print(min(cost1,cost2))
        elif x1 < 0 and y1 < 0:
            cost1 = mi*b + (mx-mi)*a
            cost3 = mx*b + (mx-mi)*a
            cost2 = x*a + y*b
            print(min(cost1,cost2))
        else:
            if x1 < y1:
                x1,y1 = y1,x1
            cost1 = y*b + (x+y)*a
            cost2 = y*a + x*a
            print(min(cost1,cost2))


