class Solution:
    def numRookCaptures(self, board: 'List[List[str]]') -> 'int':

        i_len = len(board)
        j_len = len(board[0])

        x, y = None, None
        for i in range(i_len):

            for j in range(j_len):

                if board[i][j] == "R":
                    x, y = i, j

        if x is None or y is None:
            return 0

        count = 0
        for a in range(1, j_len):
            if 0 <= y - a < j_len:
                if board[x][y - a] == 'p':
                    count += 1
                    break
                elif board[x][y-a] == 'B':
                    break
        for b in range(1, j_len):
            if 0 <= y + b < j_len:
                if board[x][y+b] == 'p':
                    count += 1
                    break
                elif board[x][y+b] == 'B':
                    break

        for c in range(1, i_len):
            if 0 <= x - c < i_len:
                if board[x-c][y] == 'p':
                    count += 1
                    break
                elif board[x-c][y] == 'B':
                    break

        for d in range(1, i_len):
            if 0 <= x + d < i_len:
                if board[x+d][y] == 'p':
                    count += 1
                    break
                elif board[x+d][y] == 'B':
                    break

        return count
