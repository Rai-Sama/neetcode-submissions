class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Horizontal check (constant r, all c's)
        # 2. Vertical check (constant c, all r's)
        # Combining both into one loop
        for i in range(9):
            cnts = dict.fromkeys(map(str, range(1,10)), 0)
            ccnts = dict.fromkeys(map(str, range(1,10)), 0)
            for j in range(9):
                if board[i][j] != "." and cnts[board[i][j]] > 0:
                    return False
                elif board[j][i] != "." and ccnts[board[j][i]] > 0:
                    return False
                else:
                    if board[i][j] != ".":
                        cnts[board[i][j]] += 1
                    if board[j][i] != ".":
                        ccnts[board[j][i]] += 1

        # Square checks - Divide into blocks of 3 and check all combinations       
        grid_groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in grid_groups:
            for l in grid_groups:
                cnts = dict.fromkeys(map(str, range(1,10)), 0)
                ccnts = dict.fromkeys(map(str, range(1,10)), 0)
                for j in i:  
                    for k in l:
                        if board[j][k] != "." and cnts[board[j][k]] > 0:
                            return False

                        if board[k][j] != "." and ccnts[board[k][j]] > 0:
                            return False
                        
                        if board[j][k] != ".":
                            cnts[board[j][k]] += 1
                        if board[k][j] != ".":
                            ccnts[board[k][j]] += 1
        return True