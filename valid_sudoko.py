def isValidSudoku(board):
    row = set()
    col = set()
    box = set()

    for i in range(len(board)):
        for j in range(len(board)):
            cell = board[i][j]
            if cell == ".": continue
            if (cell, j) in row or (i, cell) in col or (i//3, j//3, cell) in box: return False
            row.add((cell, j))
            row.add((i, cell))
            row.add((i//3, j//3, cell))
    return True




print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]

                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]

                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))