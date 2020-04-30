for t in range(int(input())):
	board = []
	for i in range(9):
		board.append(list(input()))
	
	for i in range(9):
		for j in range(9):
			if board[i][j] == "2":
				board[i][j] = "1"
	
	for i in range(9):
		for j in range(9):
			print(board[i][j], end = "")
		print()