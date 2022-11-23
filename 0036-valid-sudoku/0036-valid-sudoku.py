class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def in_three(a,b):
            temp = set()
            for i in range(a,a+3):
                for j in range(b,b+3):
                    if board[i][j] !=".":
                        if board[i][j] in temp:
                            return False
                        temp.add(board[i][j])
            return True
                        
        for i in range(len(board)):
            col = set()
            row = set()
            for j in range(len(board[i])):
                if board[i][j]!=".":
                    if int(board[i][j])<1 or int(board[i][j])>9 or board[i][j] in col:
                        return False
                    col.add(board[i][j])
                if board[j][i]!=".":
                    if int(board[j][i])<1 or int(board[j][i])>9 or board[j][i] in row:
                        return False
                    row.add(board[j][i])
        temp = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for i in temp:
            if not in_three(i[0],i[1]):
                return False
        return True