def check(i, j, board, n):
    if j != n - 1:
        if board[i][j + 1] == '1':
            return True
    else:
        return True
    if i != n - 1:
        if board[i + 1][j] == '1':
            return True
    else:
        return True

    return False


for t in range(int(input())):
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())

    isTrue = True
    for i in range(n):
        for j in range(n):
            if board[i][j] == '1':
                isTrue = check(i, j, board, n)
                if isTrue == False:
                    print("NO")
                    break
        if isTrue == False:
            break
    if isTrue:
        print("YES")
