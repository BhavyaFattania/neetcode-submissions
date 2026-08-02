class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        square = set()
        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows:
                    return False
                else:
                    rows.add(board[r][c])
            rows.clear()

            for k in range(0,9):
                if board[k][r] == ".":
                    continue
                if board[k][r] in columns:
                    return False
                else:
                    columns.add(board[k][r])
            columns.clear()
        for s in range(9):
            
            for i in range(3):
                for j in range(3):
                    row = (s//3) * 3 + i
                    col = (s % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in square:
                        return False
                    square.add(board[row][col])
            square.clear()
            
        
            

        return True

            
