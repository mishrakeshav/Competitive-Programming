for t in range(int(input())):
    n,r,c,src_row,src_col = map(int , input().split())
    directions = input()
    
    visited_rows = {src_col : [[src_row,src_row],]}
    visited_columns = {src_row : [[src_col,src_col],]}
    
    
    for d in directions:
        if d == 'N':
            initial_row = src_row
            src_row -= 1
            flag = 0
            for interval in visited_columns[src_col]:
                if src_row in range(interval[0],interval[1]+1):
                    src_row = interval[0] - 1
                    interval[0] = src_row
                    flag = 1
                    break
            if flag == 0:
                visited_columns[src_col].append([src_row,initial_row])
        elif d == 'S':
            pass 
        elif d == 'E':
            pass 
        elif d == 'W':
            pass 



    
    







for t in range(int(input())):
    n,r,c,src_row,src_col = map(int , input().split())
    directions = input()
    matrix = [[0 for i in range(c+1)] for j in range(r+1)]
    matrix[src_row][src_col] = 1
    for d in directions:
        
        if d == 'E':
            i = 1
            while matrix[src_row][src_col + i] != 0:
                i +=1 
            src_col += i
            matrix[src_row][src_col] = 1
        elif d == 'W':
            i = 1
            while matrix[src_row][src_col - i] != 0:
                i += 1
            src_col -= i 
            matrix[src_row][src_col] = 1
        elif d == 'S':
            i = 1
            while matrix[src_row + i][src_col] != 0:
                i += 1
            src_row += i
            matrix[src_row][src_col] = 1
        elif d == 'N':
            i = 1
            while matrix[src_row - i][src_col] != 0:
                i += 1
            src_row -= i
            matrix[src_row][src_col] = 1
    print(f"Case #{t+1}: {src_row} {src_col}")

    