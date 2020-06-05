from collections import namedtuple
n = int(input())
coordinates = []

class Point:
    def __init__(self,x,y,left,right,up,down):
        self.x = x
        self.y = y 
        self.left = left
        self.right = right 
        self.up = up 
        self.down = down
        
for i in range(n):
    x,y = map(int,input().split())
    coordinates.append(Point(x,y,0,0,0,0))

count = 0
for point1 in coordinates:
    # p = point1
    # print(p.x,p.y,p.left,p.right,p.up,p.down)
    if point1.left == 0 or point1.right == 0 or point1.up == 0 or point1.down == 0:
        for point2 in coordinates:
            if point1.x < point2.x and point1.y == point2:
                point1.right = 1
                point2.left = 1
            
            if point1.x > point2.x and point1.y == point2.y:
                point1.left = 1
                point2.right = 1
            
            if point1.y < point2.y and point1.x == point2.x:
                point1.up = 1
                point2.down = 1
            
            if point1.y > point2.y  and point1.x == point2.x:
                point1.down = 1
                point2.up = 1
            
for p in coordinates:
    if p.left and p.right and p.up and p.down:
        count += 1
    # print(p.x,p.y,p.left,p.right,p.up,p.down)
print(count)





    