class Solution:
    def solve(self, board, word):
        # Write your code here
        
        for i in range(len(board)):
            if "".join(board[i]).count(word) > 0 :
                return True 
        
        for i in range(len(board[0])):
            w = []
            for j in range(len(board)):

                w.append(board[j][i])
            if "".join(w).count(word) > 0:
                
                return True 
        return False

        
class Solution:
    def solve(self, board, word):
        for row in board:
            if word in ''.join(row): return True
        for col in zip(*board):
            if word in ''.join(col): return True
        return False