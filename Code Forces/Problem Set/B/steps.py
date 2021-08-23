from math import inf 


if __name__ == '__main__':
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    k = int(input())
    d = []
    count = 0 
    for i in range(k):
        dx, dy = map(int, input().split())
        xi,yi = m,n
        if dx > 0: 
            xi = (n-x)//dx 
        elif dx < 0:
            xi = (1-x)//dx
        else:
            xi = inf  
        
        if dy > 0: 
            yi = (m-y)//dy 
        elif dy < 0:
            yi = (1-y)//dy
        else:
            yi = inf  
        
        step = min(xi,yi)
        count += step 
        x = x + step*dx 
        y = y + step*dy 
    print(count)
        


        



# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     x, y = map(int, input().split())
#     k = int(input())
#     d = []
#     for i in range(k):
#         dx, dy = map(int, input().split())
#         d.append([dx, dy])
#     count = 0
#     for dx, dy in d:
#         coef = 1100000000
#         while coef >=1:
#             while isValid(n, m, x, y, dx, dy,coef):
#                 x += coef*dx
#                 y += coef*dy
#                 count += coef
#             coef //= 2 
#     print(count)
