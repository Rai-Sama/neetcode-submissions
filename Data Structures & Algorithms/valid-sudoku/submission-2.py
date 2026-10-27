class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # [set()] * 9 creates 9 references to one set
        # so had to create this way
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]: # Horizontal check
                    return False
                if board[i][j] in cols[j]: # Vertical check
                    return False
                
                box = (i//3)*3 + (j//3)
                if board[i][j] in boxes[box]: # 3X3 box check
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[box].add(board[i][j])
        
        return True