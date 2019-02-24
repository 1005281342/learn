class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    startx = i
                    starty = j
        ans = 0
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for d in direction:
            tmpx = startx
            tmpy = starty
            while 0 <= tmpx < len(board) and 0 <= tmpy < len(board[0]):
                if board[tmpx][tmpy] == 'p':
                    ans += 1
                    break
                if board[tmpx][tmpy] == 'B':
                    break
                tmpx += d[0]
                tmpy += d[1]
        return ans
