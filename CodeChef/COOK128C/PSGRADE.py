for t in range(int(input())):
    am,bm,cm,tm,a,b,c = map(int,input().split())
    t = a + b + c 
    if a >= am and b >= bm and c >= cm and t >= tm:
        print('YES')
    else:
        print('NO')