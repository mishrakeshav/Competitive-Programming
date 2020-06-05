n,m = map(int,input().split())
board = []
b = 'B'
w = 'W'
new_board = []
for i in range(n):
    board.append(input())
for i in range(n):
    new_board.append([])
    for j in range(m):
        if board[i][j] != '-':
            if i%2 == 0:
                if j%2 == 0:
                    new_board[i].append(w)
                else:
                    new_board[i].append(b)
            else:
                if j%2 == 0:
                    new_board[i].append(b)
                else:
                    new_board[i].append(w)
        else:
            new_board[i].append('-')

for i in range(n):
    for j in range(m):
        print(new_board[i][j],end = "")
    print()




