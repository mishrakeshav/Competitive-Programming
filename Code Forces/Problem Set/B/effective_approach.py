n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
positions = dict()
for i in range(n):
    positions[a[i]] = i + 1


player1 = 0
player2 = 0
for i in b:
    p = positions[i]
    player1 += p 
    player2 += n - p + 1
print(player1,player2)
